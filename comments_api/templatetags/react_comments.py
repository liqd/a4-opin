from django import template
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

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
    context = {
        'obj': obj,
        'comments_conetenttype' : comments_conetenttype,
        'contenttype': contenttype.pk,
        'pk': pk,
        'is_authenticated': is_authenticated,
        'user_name': user_name,
        'login_url': login_url
    }
    return context
