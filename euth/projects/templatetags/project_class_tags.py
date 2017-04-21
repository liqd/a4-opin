from django import template


register = template.Library()


@register.assignment_tag
def get_class(project):
    if project.is_archived:
        return 'archived'
    elif not project.is_public:
        return 'private'
    elif project.has_finished:
        return 'finished'
    elif project.days_left and project.days_left <= 5:
        return 'running-out'
    else:
        return 'public'
