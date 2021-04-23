from django import template

from adhocracy4.projects.enums import Access

register = template.Library()


@register.simple_tag
def get_class(project):
    if project.is_archived:
        return 'archived'
    elif project.access == Access.PRIVATE:
        return 'private'
    elif project.has_finished:
        return 'finished'
    elif project.days_left is not None and project.days_left <= 5:
        return 'running-out'
    else:
        return 'public'
