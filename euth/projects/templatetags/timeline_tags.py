from django import template
from django.db.models import F

register = template.Library()


@register.simple_tag
def get_sorted_date_items(project):

    phases_with_date = project.phases.filter(start_date__isnull=False)
    phases = list(phases_with_date.annotate(date=F('start_date')).values())
    events = list(project.offlineevent_set.all().values())

    object_list = phases + events
    return sorted(object_list, key=lambda k: k['date'])


@register.simple_tag
def get_past_phases_ids(project):
    return project.past_phases.values_list('id', flat=True)
