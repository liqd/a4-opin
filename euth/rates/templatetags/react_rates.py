from django import template
from django.conf import settings
from django.contrib.contenttypes.models import ContentType

register = template.Library()


@register.inclusion_tag('rates/react_rates.html', takes_context=True)
def react_rates(context, obj):

    login_url = settings.LOGIN_URL + '?next=' + context['request'].path

    rates_contenttype = ContentType.objects.get(
        app_label="euth_rates", model="rate")

    contenttype = ContentType.objects.get_for_model(obj)
    pk = obj.pk

    is_authenticated = int(context['request'].user.is_authenticated())

    context = {
        'login_url': login_url,
        'rates_contenttype': rates_contenttype,
        'contenttype': contenttype,
        'object_id': pk,
        'is_authenticated': is_authenticated
    }

    return context
