from django import template
from django.contrib.contenttypes.models import ContentType

register = template.Library()

@register.inclusion_tag('comments_api/react_comments.html', takes_context=True)
def react_comments(context, obj):

	contenttype = ContentType.objects.get_for_model(obj)
	pk = obj.pk
	is_authenticated = context['request'].user.is_authenticated()
	user_name = context['request'].user.username
	return {'contenttype': contenttype.pk, 'pk': pk, 'is_authenticated':is_authenticated, 'user_name': user_name}