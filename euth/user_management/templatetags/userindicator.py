from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.inclusion_tag('user_management/indicator.html', takes_context=True)
def userindicator(context, next_action=None):
    request = context['request']
    if not next_action:
        next_action = request.get_full_path()
        if next_action == reverse('login') or next_action == reverse('logout'):
            reverse('process-listing')

    context = template.RequestContext(
        request,
        {
            'user': request.user,
            'next_action': next_action or request.get_full_path()
        })
    return context
