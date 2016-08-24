from django import template
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

from euth.rates import models as rate_models

register = template.Library()


@register.inclusion_tag('rates/react_rates.html', takes_context=True)
def react_rates(context, obj):

    login_url = reverse('login') + '?next=' + context['request'].path

    contenttype = ContentType.objects.get_for_model(obj)

    user = context['request'].user

    if user.is_authenticated():
        authenticated_as = user.username
    else:
        authenticated_as = None

    try:
        user_rate = rate_models.Rate.objects.get(
            content_type=contenttype, object_pk=obj.pk, user=user)
        user_rate_value = user_rate.value
        user_rate_id = user_rate.pk
    except:
        user_rate_value = None
        user_rate_id = -1

    context = {
        'login_url': login_url,
        'contenttype': contenttype.pk,
        'object_id': obj.pk,
        'authenticated_as': authenticated_as,
        'positive_rates': obj.positive_rates,
        'negative_rates': obj.negative_rates,
        'user_rate': user_rate_value,
        'user_rate_id': user_rate_id,
    }

    return context
