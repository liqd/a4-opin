from django.core.urlresolvers import reverse

_usermanagement_views = [ 'login', 'logout', 'register', 'reset_request' ]

def sanatize_next(request, override_next=None):
    """
    Get appropriate next value for the given request
    """
    if override_next:
        next_action = override_next
    else:
        next_action = request.get_full_path()

    invalid_next_views = [ reverse(u) for u in _usermanagement_views ]
    if request.path in invalid_next_views:
        next_action = request.GET.get('next')\
            or request.POST.get('next')\
            or '/'
    return next_action
