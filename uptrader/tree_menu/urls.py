from django.urls import path, re_path

from .views import MenuView

urlpatterns = [
    path('', MenuView.as_view(), name='home'),
    re_path(r'^(?!__debug__/)(?P<path>.+/)$',
            MenuView.as_view(), name='menu_page'),
]
