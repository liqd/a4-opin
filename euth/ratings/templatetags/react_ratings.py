from django import template
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

from euth.ratings import models as rating_models

register = template.Library()


@register.inclusion_tag('ratings/react_ratings.html', takes_context=True)
def react_ratings(context, obj):
    request = context['request']
    user = request.user

    contenttype = ContentType.objects.get_for_model(obj)
    permission = '{ct.app_label}.rate_{ct.model}'.format(ct=contenttype)
    has_rate_permission = user.has_perm(permission, obj)

    login_url = reverse('account_login') + '?next=' + request.path

    if user.is_authenticated():
        authenticated_as = user.username
    else:
        authenticated_as = None

    try:
        user_rating = rating_models.Rating.objects.get(
            content_type=contenttype, object_pk=obj.pk, user=user)
        user_rating_value = user_rating.value
        user_rating_id = user_rating.pk
    except:
        user_rating_value = None
        user_rating_id = -1

    context = {
        'login_url': login_url,
        'contenttype': contenttype.pk,
        'object_id': obj.pk,
        'authenticated_as': authenticated_as,
        'positive_ratings': obj.positive_ratings,
        'negative_ratings': obj.negative_ratings,
        'user_rating': user_rating_value,
        'user_rating_id': user_rating_id,
        'is_read_only': not has_rate_permission,
    }

    return context
