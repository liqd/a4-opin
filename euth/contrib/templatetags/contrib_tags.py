from django import template

register = template.Library()


@register.simple_tag
def combined_url_parameter(request_query_dict, **kwargs):
    combined_query_dict = request_query_dict.copy()
    for key in kwargs:
        combined_query_dict.setlist(key, [kwargs[key]])
    encoded_parameter = '?' + combined_query_dict.urlencode()
    return encoded_parameter


@register.simple_tag
def limited_paginator(page_obj):
    ADDITIONAL_PAGES = 3

    current_index = page_obj.number - 1
    last_index = page_obj.paginator.num_pages
    start_index = current_index - ADDITIONAL_PAGES if \
        current_index > ADDITIONAL_PAGES else 0
    end_index = current_index + ADDITIONAL_PAGES if \
        current_index < last_index - ADDITIONAL_PAGES else last_index

    return page_obj.paginator.page_range[start_index:end_index]
