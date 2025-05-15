from ..models import MenuItem


def get_menu_items(menu_name):
    """Получение пунктов меню."""
    items = MenuItem.objects.filter(
        menu__name=menu_name
    ).select_related(
        'parent',
        'menu'
    )

    return items


def get_active_item(menu_items, current_path):
    """Получение активного пункта меню."""
    for item in menu_items:
        if item.get_url() == current_path:
            return item


def get_selected_ids(active_item):
    """Получение id выбранных пунктов меню."""
    selected_ids = set()
    parent = active_item.parent
    while parent:
        selected_ids.add(parent.id)
        parent = parent.parent

    return selected_ids
