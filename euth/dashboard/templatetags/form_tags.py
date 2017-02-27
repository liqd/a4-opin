from django import template

from django.conf import settings
from adhocracy4 import phases

register = template.Library()


@register.assignment_tag
def get_checkbox_label(form, fieldname):
    return form.get_checkbox_label(fieldname)


@register.assignment_tag
def add(number1, number2):
    return number1 + number2


@register.assignment_tag
def next(some_list, current_index):
    try:
        return some_list[int(current_index) + 1]
    except:
        return ''


@register.assignment_tag
def getPhaseName(type):
    name = phases.content.__getitem__(type).name
    return name

@register.assignment_tag
def getAllowedFileTypes():
    fileformats = settings.FILE_ALIASES['*']['fileformats']
    return ', '.join([name for name, mimetype in fileformats])
