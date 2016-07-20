import bleach

from django.conf import settings


def clean_html_all(text):
    return bleach.clean(text,
                        tags=[], attributes={}, styles=[], strip=True)


def clean_html_field(text):
    allowed_tags = settings.BLEACH_LIST['default']['tags']
    allowed_attrs = settings.BLEACH_LIST['default']['attributes']
    return bleach.clean(text,
                        tags=allowed_tags,
                        attributes=allowed_attrs,
                        styles=[],
                        strip=True)
