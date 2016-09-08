from django import template

from .. import sanatize_next

register = template.Library()


@register.inclusion_tag(
    'euth_users/indicator_menu.html',
    takes_context=True)
def userindicator_menu(context):
    request = context['request']
    context = template.RequestContext(
        request,
        {
            'user': request.user,
            'next_action': sanatize_next(request)
        })
    return context
