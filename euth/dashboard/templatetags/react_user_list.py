import json

from django import template
from django.db.models.functions import Lower
from django.utils.html import format_html
from rest_framework.serializers import ListSerializer

from euth.users.serializers import UserWithMailSerializer

register = template.Library()


@register.simple_tag()
def react_user_list(users, project, identifier):
    users = users.order_by(Lower('username'))
    user_list = ListSerializer(users, child=UserWithMailSerializer()).data

    format_strings = {
        'users': json.dumps(user_list),
        'project': project.pk,
        'listen_to': identifier,
    }

    return format_html(
        (
            '<span data-euth-widget="userlist"'
            ' data-users="{users}"'
            ' data-project="{project}"'
            ' data-listen-to="{listen_to}"></span>'
        ),
        **format_strings
    )
