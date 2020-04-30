from django import template
from easy_thumbnails.templatetags.thumbnail import thumbnail_url

register = template.Library()


@register.simple_tag()
def get_avatar(user, size_alias):
    if user.avatar:
        return thumbnail_url(user.avatar, size_alias)
    else:
        return user.avatar_fallback
