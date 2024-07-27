from django import template
from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path

    def get_menu_items(parent=None):
        items = MenuItem.objects.filter(parent=parent)
        return [
            {
                'item': item,
                'children': get_menu_items(item),
                'is_active': current_path == item.get_url(),
            }
            for item in items
        ]

    menu_items = get_menu_items()
    return {'menu_items': menu_items}
