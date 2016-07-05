from django import template
from django.core.urlresolvers import reverse
from django.core.urlresolvers import resolve
from django.http import Http404
from django.utils import translation



register = template.Library()




@register.simple_tag(takes_context=True)
def translate_url(context, lang=None, *args, **kwargs):
    """
    Get active page's url by a specified language
    Usage: {% translate_url 'en' %}
    """
    path = context['request'].path
    try:
        url_parts = resolve(path)
        url = path
        cur_language = translation.get_language()
        try:
            translation.activate(lang)
            url = reverse(url_parts.view_name, kwargs=url_parts.kwargs)
        except:
            if url_parts.args:
                url = '/' + lang + '/' + url_parts.args[0]
            else:
                url = '/'  + lang + '/'
        finally:
            translation.activate(cur_language)
    except Http404:
        url = '/'  + lang + '/'

    return "%s" % url
