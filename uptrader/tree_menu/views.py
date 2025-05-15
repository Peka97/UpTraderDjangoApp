from django.shortcuts import render
from django.views import View


def page_view(request, path, *args, **kwargs):
    template_name = 'tree_menu/page.html'
    return render(request, template_name)


class MenuView(View):
    """
    Единое (с демонстрационной целью) представление для всех страниц меню.
    """

    def get(self, request, *args, **kwargs):
        path = kwargs.get('path', '')
        template_name = 'tree_menu/page.html'
        context = {
            'request': request,
            'path': path,
        }

        return render(request, template_name, context)
