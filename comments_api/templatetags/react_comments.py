import json

from django import template
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.utils.translation import ugettext as _

register = template.Library()


@register.inclusion_tag('comments_api/react_comments.html', takes_context=True)
def react_comments(context, obj):

    login_url = settings.LOGIN_URL + '?next=' + context['request'].path

    comments_conetenttype = content_type = ContentType.objects.get(
        app_label="django_comments", model="comment")

    contenttype = ContentType.objects.get_for_model(obj)
    pk = obj.pk

    is_authenticated = int(context['request'].user.is_authenticated())
    user_name = context['request'].user.username

    translations = {
        'comments_i18n_sgl': _("Comment"),
        'comments_i18n_pl': _("Comments"),
        'i18n_your_comment': _("Your comment here"),
        'i18n_please_loggin_to_comment': _("Please login to comment")
    }

    translations_json = json.dumps({
        'translations': translations,
    }, cls=DjangoJSONEncoder)

    context = {
        'obj': obj,
        'comments_conetenttype': comments_conetenttype,
        'contenttype': contenttype.pk,
        'pk': pk,
        'is_authenticated': is_authenticated,
        'user_name': user_name,
        'login_url': login_url,
        'translations': translations_json
    }

    return context
