from django import template

register = template.Library()


@register.assignment_tag
def get_checkbox_label(form, fieldname):
    return form.get_checkbox_label(fieldname)
