from django import template
from django.utils.safestring import mark_safe

from ..services.tree_builder import build_menu_tree
from ..services.helpers import get_menu_items, get_active_item, get_selected_ids

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    """Рисует дерево меню."""
    request = context.get('request')
    if not request:
        return ''

    current_path = request.path_info

    menu_items = get_menu_items(menu_name)
    active_item = get_active_item(menu_items, current_path)

    selected_ids = set()
    if active_item:
        selected_ids = get_selected_ids(active_item)

    return mark_safe(build_menu_tree(menu_items, current_path, selected_ids))
