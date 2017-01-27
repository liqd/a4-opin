import json

from django import template
from django.db.models.functions import Lower
from django.utils.safestring import mark_safe
from rest_framework.serializers import ListSerializer

from euth.users.serializers import UserWithMailSerializer

register = template.Library()


@register.simple_tag()
def react_user_list(users, identifier=None):
    users = users.order_by(Lower('username'))
    user_list = ListSerializer(users, child=UserWithMailSerializer()).data

    mountpoint = 'users_{}'.format(id(users))

    format_strings = {
        'users': json.dumps(user_list),
        'mountpoint': mountpoint,
        'listen_to': '',
    }

    if identifier:
        format_strings['listen_to'] = ', "{}"'.format(identifier)

    return mark_safe((
        '<span id="{mountpoint}"></span><script>window.opin.renderUserList('
        '"{mountpoint}", {users}{listen_to})</script>')
                     .format(**format_strings)
    )
