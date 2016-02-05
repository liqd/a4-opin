from django import template
#from django_feedparser.settings import *
from home.models import NavigationMenu
register = template.Library()


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    return context['request'].site.root_page


@register.inclusion_tag('tags/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu().specific()

    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        'request': context['request'],
    }


@register.assignment_tag(takes_context=False)
def load_site_menu(menu_name):
    menu = NavigationMenu.objects.filter(menu_name=menu_name)

    if menu:
        return menu[0].menu_items.all()
    else:
        return None
