from django import template, utils
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

from ..models import Comment

register = template.Library()


@register.inclusion_tag('comments/react_comments.html', takes_context=True)
def react_comments(context, obj):
    request = context['request']

    user = request.user
    is_authenticated = int(user.is_authenticated())
    user_name = user.username

    contenttype = ContentType.objects.get_for_model(obj)
    permission = '{ct.app_label}.comment_{ct.model}'.format(ct=contenttype)
    has_comment_permission = user.has_perm(permission, obj)

    login_url = reverse('account_login') + '?next=' + context['request'].path
    comments_contenttype = ContentType.objects.get_for_model(Comment)
    pk = obj.pk

    language = utils.translation.get_language()

    context = {
        'obj': obj,
        'comments_contenttype': comments_contenttype,
        'contenttype': contenttype.pk,
        'pk': pk,
        'is_authenticated': is_authenticated,
        'user_name': user_name,
        'login_url': login_url,
        'language': language,
        'is_read_only': not has_comment_permission,
    }

    return context
