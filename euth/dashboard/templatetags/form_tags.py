from django import template

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
