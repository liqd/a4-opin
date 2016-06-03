from django.conf.urls import url


def processUrl(suburl, views, **kwargs):
    return url(r'^(?P<process_name>\w+)/' + suburl, views, **kwargs)
