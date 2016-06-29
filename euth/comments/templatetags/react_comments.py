import json

from django import template
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.utils.translation import ugettext as _

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

    translations = {
        'comments_i18n_sgl': _('Comment'),
        'comments_i18n_pl': _('Comments'),
        'i18n_your_comment': _('Your comment here'),
        'i18n_please_loggin_to_comment': _('Please login to comment'),
        'i18n_answer': _('Answer'),
        'i18n_post': _('Post'),
        'i18n_cancel': _('Cancel'),
        'i18n_edit':_('Edit'),
        'i18n_report':_('Report'),
        'i18n_delete':_('Delete'),
        'i18n_abort':_('Abort'),
        'i18n_ask_delete':_('Do you really want to delete this comment?'),
    }

    translations_json = json.dumps({
        'translations': translations,
    }, cls=DjangoJSONEncoder)

    context = {
        'obj': obj,
        'comments_contenttype': comments_contenttype,
        'contenttype': contenttype.pk,
        'pk': pk,
        'is_authenticated': is_authenticated,
        'user_name': user_name,
        'login_url': login_url,
        'translations': translations_json
    }

    return context
