from django.urls import Resolver404
from django.urls import resolve
from django.utils.http import url_has_allowed_host_and_scheme

USERNAME_REGEX = r'^[\w]+[ \w.@+-]*$'


def _get_account_url_names():
    from allauth.account import urls
    return tuple([url.name for url in urls.urlpatterns])


def sanitize_next(request):
    """
    Get appropriate next value for the given request
    """
    try:
        url_name = resolve(request.path).url_name
    except Resolver404:
        url_name = '__invalid_url_name__'

    if url_name in _get_account_url_names():
        nextparam = request.GET.get('next') or request.POST.get('next')
        next = nextparam \
            if url_has_allowed_host_and_scheme(nextparam, allowed_hosts=None) \
            else '/'
    else:
        next = request.get_full_path()
    return next
