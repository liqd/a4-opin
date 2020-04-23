from django import template

from euth.ideas.models import Idea

register = template.Library()


@register.simple_tag
def get_range(number, listcount):
    if number < 3:
        return range(1, 6)
    elif number > listcount - 2:
        return range(listcount - 4, listcount + 1)
    else:
        return range(number - 2, number + 3)


@register.simple_tag
def is_idea_list(module):
    return Idea.objects.filter(module=module).count() > 0


@register.simple_tag
def combined_url_parameter(request_query_dict, **kwargs):
    combined_query_dict = request_query_dict.copy()
    for key in kwargs:
        combined_query_dict.setlist(key, [kwargs[key]])
    encoded_parameter = '?' + combined_query_dict.urlencode()
    return encoded_parameter
