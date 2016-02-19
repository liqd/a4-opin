from django import template
from django.core.urlresolvers import reverse
from django.core.urlresolvers import resolve
from django.http import Http404
from django.utils import translation

register = template.Library()


@register.simple_tag(takes_context=True, name='translate_url')
def do_translate_url(context, language):
	try:
		view = resolve(context['request'].path)
		if view.args:
			url = '/' + language + '/' + view.args[0]
		else:
			url = '/'  + language + '/'
	except Http404:
		url = '/'  + language + '/'
	return url
