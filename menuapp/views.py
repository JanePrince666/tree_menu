from django.views import View
from django.shortcuts import render


class MenuView(View):
    template_name = 'menu/home_page.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)
