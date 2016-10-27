from django import template
from django.forms import CheckboxInput

register = template.Library()


@register.filter(name='is_checkbox')
def is_checkbox(field):
    checkbox_class_name = CheckboxInput().__class__.__name__

    return field.field.widget.__class__.__name__ == checkbox_class_name


@register.assignment_tag
def get_checkbox_label(form, fieldname):
    return form.get_checkbox_label(fieldname)
