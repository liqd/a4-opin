from django import template

register = template.Library()


@register.simple_tag
def selected(request, pattern):
    path = request.path
    if path == pattern:
        return 'selected'
    return ''


@register.assignment_tag
def phase_name(index, phase_list):
    print(index)
    print(phase_list)
    return phase_list[index]
