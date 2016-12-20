import json

from django import template
from django.contrib.contenttypes.models import ContentType
from django.utils.safestring import mark_safe

from euth.ratings import models as rating_models

register = template.Library()


@register.simple_tag(takes_context=True)
def react_ratings(context, obj):
    request = context['request']
    user = request.user

    contenttype = ContentType.objects.get_for_model(obj)
    permission = '{ct.app_label}.rate_{ct.model}'.format(ct=contenttype)
    has_rate_permission = user.has_perm(permission, obj)

    if user.is_authenticated():
        authenticated_as = user.username
    else:
        authenticated_as = None
    user_rating = rating_models.Rating.objects.filter(
        content_type=contenttype, object_pk=obj.pk, creator=user.pk).first()
    if user_rating:
        user_rating_value = user_rating.value
        user_rating_id = user_rating.pk
    else:
        user_rating_value = None
        user_rating_id = -1

    mountpoint = 'ratings_for_{contenttype}_{pk}'.format(
        contenttype=contenttype.pk,
        pk=obj.pk
    )
    attributes = {
        'contentType': contenttype.pk,
        'objectId': obj.pk,
        'authenticatedAs': authenticated_as,
        'positiveRatings': obj.positive_rating_count,
        'negativeRatings': obj.negative_rating_count,
        'userRating': user_rating_value,
        'userRatingId': user_rating_id,
        'isReadOnly': not has_rate_permission,
        'style': 'ideas',
    }

    return mark_safe((
        '<div id={mountpoint}></div><script>window.opin.renderRatings('
        '{mountpoint}, {attributes})</script>').format(
            attributes=json.dumps(attributes),
            mountpoint=json.dumps(mountpoint)
        )
    )
