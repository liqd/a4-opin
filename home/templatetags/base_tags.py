import bleach
import feedparser
from dateutil import parser
from django import template
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from home.models.snippets import NavigationMenu

register = template.Library()


@register.simple_tag(takes_context=True)
def get_page_name(context, page):
    page_type = page.content_type
    try:
        page_object = page_type.get_object_for_this_type(id=page.id)
        if hasattr(page_object, 'translated_title'):
            return page_object.translated_title
        else:
            return page
    except ObjectDoesNotExist:
        return page


@register.simple_tag(takes_context=True)
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


@register.inclusion_tag('includes/rss_import.html', takes_context=True)
def import_rss(context, rss_import):

    feeds = feedparser.parse(rss_import.url)
    entries = feeds.entries[:2]

    result = []

    for entry in entries:
        try:
            published = parser.parse(entry["published"])
        except Exception:
            published = ''

        result.append({
            'published': published,
            'title': entry.title,
            'link': entry.link,
            'description': bleach.clean(entry.summary,
                                        tags=[],
                                        attributes={},
                                        styles=[],
                                        strip=True
                                        )
        }
        )

    return {
        'title': rss_import.translated_rss_title,
        'entries': result
    }


@register.simple_tag(takes_context=False)
def load_site_menu(menu_name):
    menu = NavigationMenu.objects.filter(menu_name=menu_name)

    if menu:
        return menu[0].menu_items.all()
    else:
        return None


@register.filter(name='clear_class')
def clear_class(columns_per_row, count):
    if (count - 1) % (12 / int(columns_per_row)) == 0:
        return "m-clear"
    else:
        return ""


@register.simple_tag
def settings_value(name):
    return getattr(settings, name, "")
