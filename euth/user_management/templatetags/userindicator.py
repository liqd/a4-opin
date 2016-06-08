from django import template
from .. import sanatize_next

register = template.Library()


@register.inclusion_tag('user_management/indicator.html', takes_context=True)
def userindicator(context, next_action=None):
    request = context['request']
    context = template.RequestContext(
        request,
        {
            'user': request.user,
            'next_action': sanatize_next(request, next_action)
        })
    return context
