from django import template
from django.conf import settings

from adhocracy4 import phases

register = template.Library()


@register.simple_tag
def add(number1, number2):
    return number1 + number2


@register.simple_tag
def next(some_list, current_index):
    try:
        return some_list[int(current_index) + 1]
    except (IndexError, TypeError, ValueError):
        return ''


@register.simple_tag
def getPhaseName(type):
    name = phases.content.__getitem__(type).name
    return name


@register.simple_tag
def getAllowedFileTypes():
    fileformats = settings.FILE_ALIASES['*']['fileformats']
    return ', '.join([name for name, mimetype in fileformats])


@register.simple_tag
def get_disabled(project):
    return 'disabled' if project and project.is_archived else ''
