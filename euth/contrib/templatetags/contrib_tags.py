from django import template
from django.utils.translation import ugettext_lazy as _

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


@register.simple_tag
def get_howto_items():
    steps_header = 'How can I register my organisation and start a project?'
    step1_text = 'Register as a user by following the steps on the left to '\
        'create an account.'
    step2_text = 'Send us en e-mail via info@opin.me and provide your '\
        'username, email address, organisation name and its location, '\
        'a short description of your project.'
    step3_text = 'Since we are in beta for the moment, we cannot accept all'\
        'requests to use OPIN. You will receive a reply within 48 hours.'
    steps = [
        {
            'num': 1,
            'header': _(steps_header),
            'img': 'images/step1-2x-noshadow.png',
            'subheader': _('1. Register an account'),
            'text': _(step1_text)
        },
        {
            'num': 2,
            'header': _(steps_header),
            'img': 'images/step2-2x-noshadow.png',
            'subheader': _('2. Contact us'),
            'text': _(step2_text)
        },
        {
            'num': 3,
            'header': _(steps_header),
            'img': 'images/step3-2x-noshadow.png',
            'subheader': _('3. We will review your request.'),
            'text': _(step3_text)
        },
    ]
    return steps
