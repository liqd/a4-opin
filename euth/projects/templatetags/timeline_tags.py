from django import template
from django.db.models import F

register = template.Library()


@register.assignment_tag
def get_sorted_date_items(project):

    phases = list(project.phases.all().annotate(date=F('start_date')).values())
    events = list(project.offlineevent_set.all().values())

    object_list = phases + events
    return sorted(object_list, key=lambda k: k['date'])


@register.assignment_tag
def get_past_phases_ids(project):
    return project.past_phases.values('id')
