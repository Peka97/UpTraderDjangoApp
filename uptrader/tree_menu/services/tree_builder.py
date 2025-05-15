def build_menu_tree(menu_items, current_path, selected_ids, parent=None, level=0):
    """
    Построение дерева меню.
    """

    items = [
        item for item in menu_items if item.parent_id ==
        (parent.id if parent else None)
    ]
    items = sorted(items, key=lambda x: x.order)

    if not items:
        return ''

    return build_html_menu_tree(menu_items, items, current_path, selected_ids, level)


def build_html_menu_tree(menu_items, items, current_path, selected_ids, level):
    """
    Построение дерева меню с HTML.
    """
    result = ['<ul>']

    for item in items:
        item_url = item.get_url()
        item_is_selected = item_url == current_path
        item_has_selected_child = has_selected_child(
            item, menu_items, current_path)

        should_expand = item_is_selected or item_has_selected_child or (
            item.id in selected_ids)

        result.append(f'<li class="{"active" if item_is_selected else ""}">')
        result.append(f'<a href="{item_url}">{item.title}</a>')

        if should_expand:
            new_selected_ids = selected_ids.union({item.id})
            children = build_menu_tree(
                menu_items,
                current_path,
                new_selected_ids,
                item,
                level+1
            )
            result.append(children)

        result.append('</li>')

    result.append('</ul>')
    return ''.join(result)


def has_selected_child(item, menu_items, current_path):
    for child in menu_items:
        if child.parent_id == item.id and child.get_url() == current_path:
            return True

    return False
