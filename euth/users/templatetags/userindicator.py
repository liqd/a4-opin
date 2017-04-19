from django import template

from .. import sanitize_next

register = template.Library()


@register.inclusion_tag('euth_users/indicator_menu.html', takes_context=True)
def userindicator_menu(context):
    context['redirect_field_value'] = sanitize_next(context['request'])
    return context
