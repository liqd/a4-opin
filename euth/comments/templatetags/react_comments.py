import json

from django import template
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django import utils

register = template.Library()


@register.inclusion_tag('comments/react_comments.html', takes_context=True)
def react_comments(context, obj):

    login_url = settings.LOGIN_URL + '?next=' + context['request'].path

    comments_contenttype = ContentType.objects.get(
        app_label="comments", model="comment")

    contenttype = ContentType.objects.get_for_model(obj)
    pk = obj.pk

    is_authenticated = int(context['request'].user.is_authenticated())
    user_name = context['request'].user.username

    language = utils.translation.get_language()

    context = {
        'obj': obj,
        'comments_contenttype': comments_contenttype,
        'contenttype': contenttype.pk,
        'pk': pk,
        'is_authenticated': is_authenticated,
        'user_name': user_name,
        'login_url': login_url,
        'language': language
    }

    return context
