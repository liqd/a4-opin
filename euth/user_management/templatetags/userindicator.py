from django import template
from .. import sanatize_next

from ..forms import RegisterForm, LoginForm

register = template.Library()


@register.inclusion_tag('user_management/indicator_menu.html', takes_context=True)
def userindicator_menu(context, next_action=None):
    request = context['request']
    context = template.RequestContext(
        request,
        {
            'user': request.user,
            'next_action': sanatize_next(request, next_action),
            'register_form': RegisterForm(None),
            'login_form': LoginForm(None),
        })
    return context
