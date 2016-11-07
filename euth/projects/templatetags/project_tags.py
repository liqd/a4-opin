from django.utils.translation import ungettext
from django.utils.translation import ugettext as _
from django import template

register = template.Library()


@register.assignment_tag
def get_days(number):
    if number and number >= 1 and number <= 5:
        text = ungettext(
            '%(number)d day left',
            '%(number)d days left',
            number) % {
            'number': number,
        }
        return text
    elif number == 0:
        return _('a few hours left')
    else:
        return ''

@register.assignment_tag
def get_class(project):
    if project.has_finished:
        return 'finished'
    elif not project.is_public:
        return 'private'
    elif project.days_left and project.days_left <= 5:
        return 'running-out'
    else:
        return 'public'
