from django.conf import settings
from django.utils.html import format_html
from wagtail.core import hooks


@hooks.register('insert_editor_css')
def editor_css():
    return format_html('<link rel="stylesheet" href="'
                       + settings.STATIC_URL
                       + 'wagtail_admin.css">')
