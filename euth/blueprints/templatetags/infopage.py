from django import template

from euth.offlinephases import phases

register = template.Library()


@register.assignment_tag
def get_project(helppages, blueprint):
    return getattr(helppages, blueprint.type, None)


@register.assignment_tag
def get_offlinephase():
    return phases.OfflinePhase
