import json

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag()
def react_follows(project):
    attributes = {
        'project': project.slug
    }

    mountpoint = 'follow_{}'.format(project.slug)

    return mark_safe((
        '<div id={mountpoint}></div><script>window.opin.renderFollow('
        '{mountpoint}, {attributes})</script>').format(
            attributes=json.dumps(attributes),
            mountpoint=json.dumps(mountpoint)
        )
    )
