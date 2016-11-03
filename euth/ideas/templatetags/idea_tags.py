from django import template

register = template.Library()


@register.assignment_tag
def get_range(number, listcount):
    if number < 3:
        return range(1, 6)
    elif number > listcount - 2:
        return range(listcount-4, listcount+1)
    else:
        return range(number-2, number+3)
