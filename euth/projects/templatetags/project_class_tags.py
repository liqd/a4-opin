from django import template
from django.utils import timezone
from django.utils.translation import gettext as _
from django.utils.translation import ngettext

from adhocracy4.projects.enums import Access

register = template.Library()


def days_left(project):
    """
    Replaces the project property days_left that was removed from a4.
    Still uses the active_phase property, which is deprecated.
    """
    active_phase = project.active_phase
    if active_phase:
        today = timezone.now().replace(hour=0, minute=0, second=0)
        time_delta = active_phase.end_date - today
        return time_delta.days
    return None


@register.simple_tag
def get_class(project):
    if project.is_archived:
        return 'archived'
    elif (project.access == Access.PRIVATE
          or project.access == Access.SEMIPUBLIC):
        return 'private'
    elif project.has_finished:
        return 'finished'
    elif days_left(project) is not None and days_left(project) <= 5:
        return 'running-out'
    else:
        return 'public'


@register.simple_tag
def get_days(project):
    number = days_left(project)
    if number and number >= 1 and number <= 5:
        text = ngettext(
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
