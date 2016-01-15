from django import template
from django.core.urlresolvers import reverse
from django.core.urlresolvers import resolve
from django.utils import translation

register = template.Library()


@register.simple_tag(takes_context=True, name='translate_url')
def do_translate_url(context, language):
	view = resolve(context['request'].path)
	url = '/' + language + '/' + view.args[0]
	return url
