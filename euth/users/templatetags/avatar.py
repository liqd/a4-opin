from django import template

register = template.Library()


@register.simple_tag()
def get_avatar(user, size_alias):
    return user.avatar_fallback
