from django import template

from .. import sanatize_next

register = template.Library()


@register.inclusion_tag('euth_users/indicator_menu.html', takes_context=True)
def userindicator_menu(context):
    context['next_action'] = sanatize_next(context['request'])
    return context
