from django import template

register = template.Library()


@register.simple_tag
def get_project(helppages, blueprint):
    return getattr(helppages, blueprint.type, None)
