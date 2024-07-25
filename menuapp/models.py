from django.db import models
from django.utils.text import slugify


class MenuItem(models.Model):
    title = models.CharField(max_length=200)  # The title of the menu item
    url = models.CharField(max_length=200, blank=True, null=True)  # Explicit URL
    named_url = models.CharField(max_length=200, blank=True, null=True)  # Named URL
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """
        Override the save method to automatically generate the URL based on the title or named_url.

        If neither is provided, a URL is generated from the title.
        If a parent exists, the parent's URL is prepended to the current item's URL.
        """
        # Generate URL automatically based on title or named_url
        if not self.url:
            if self.named_url:
                self.url = f"/{slugify(self.named_url)}/"
            else:
                self.url = f"/{slugify(self.title)}/"

        # Append parent URL if a parent exists
        if self.parent:
            self.url = f"{self.parent.url.rstrip('/')}/{self.url.lstrip('/')}"

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Returns the full URL for navigating to the menu item."""
        return self.url

    def get_ancestors(self, include_self=False):
        """
        Returns a list of all parent elements (ancestors).

        Args:
            include_self (bool): If True, include the current item in the returned list.

        Returns:
            list: A list of ancestor MenuItem instances, ordered from root to current item.
        """
        ancestors = []
        current = self
        while current.parent is not None:
            ancestors.append(current.parent)
            current = current.parent
        if include_self:
            ancestors.append(self)
        return ancestors[::-1]  # Return in order from root to current item

    def __str__(self):
        """Returns the string representation of the MenuItem, which is its title."""
        return self.title
