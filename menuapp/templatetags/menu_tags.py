from django import template
from django.template.loader import render_to_string
from ..models import MenuItem

register = template.Library()


def find_active_depth(item, current_url, depth=0):
    """
    Function to find the nesting level of the active element.

    Args:
        item (MenuItem): The current menu item.
        current_url (str): The current URL.
        depth (int, optional): The current nesting depth. Defaults to 0.

    Returns:
        int: The nesting depth of the active element, or 0 if not found.
    """
    if current_url == item.get_absolute_url():
        return depth
    for child in item.children.all():
        result = find_active_depth(child, current_url, depth + 1)
        if result != 0:
            return result
    return 0


def build_menu_tree(item, current_url, active_depth, current_depth=None):
    """
    Recursive function to build the menu tree.

    Args:
        item (MenuItem): The current menu item.
        current_url (str): The current URL.
        active_depth (int): The nesting depth of the active element.
        current_depth (int, optional): The current nesting depth. Defaults to None.

    Returns:
        dict: A dictionary representing the subtree for the current menu item.
    """
    if current_depth is None:
        current_depth = 0
    is_active = current_url == item.get_absolute_url()  # Check if the current element is active
    # Create a structure for the current element
    subtree = {
        'item': item,
        'is_active': is_active,
        'children': []
    }
    # Get all children of the current element
    children = item.children.all()

    # Add children if the current nesting level does not exceed the active element's nesting level
    if (current_depth < active_depth) or is_active:
        # Increase the current nesting level
        current_depth += 1
        for child in children:
            subtree['children'].append(build_menu_tree(child, current_url, active_depth, current_depth))

    return subtree


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    """
    Template tag to render the menu.

    Args:
        context (dict): The context passed from the template.
        menu_name (str): The name of the menu to render.

    Returns:
        str: The rendered HTML for the menu.
    """
    # Get the current URL
    current_url = context['request'].path

    # Get the menu item by name
    menu_item = MenuItem.objects.filter(title=menu_name).prefetch_related('children').first()
    menu_hierarchy = []
    active_depth = find_active_depth(menu_item, current_url)
    menu_hierarchy.append(build_menu_tree(menu_item, current_url, active_depth))

    return render_to_string('menu/menu.html', {'menu_items': menu_hierarchy})
