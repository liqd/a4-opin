from django.core.urlresolvers import resolve


def _get_invalid_url_names():
    from allauth.account import urls
    return tuple([url.name for url in urls.urlpatterns])


def sanatize_next(request):
    """
    Get appropriate next value for the given request
    """
    if resolve(request.path).url_name in _get_invalid_url_names():
        next = request.GET.get('next') or request.POST.get('next') or '/'
    else:
        next = request.get_full_path()
    return next
