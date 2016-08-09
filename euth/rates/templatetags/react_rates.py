from django import template
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

register = template.Library()


@register.inclusion_tag('rates/react_rates.html', takes_context=True)
def react_rates(context, obj):

    login_url = reverse('login') + '?next=' + context['request'].path

    contenttype = ContentType.objects.get_for_model(obj)
    pk = obj.pk

    is_authenticated = int(context['request'].user.is_authenticated())
    user_name = context['request'].user.username

    context = {
        'login_url': login_url,
        'contenttype': contenttype.pk,
        'object_id': pk,
        'is_authenticated': is_authenticated,
        'user_name': user_name
    }

    return context
