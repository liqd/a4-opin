from django import template

register = template.Library()


@register.simple_tag
def selected(request, pattern):
    path = request.path
    if path == pattern:
        return 'selected'
    return ''
