from django.core.urlresolvers import reverse


def sanatize_next(request, override_next=None):
    """
    Get appropriate next value for the given request
    """
    if override_next:
        next_action = override_next
    else:
        next_action = request.get_full_path()

    if request.path in [reverse('login'), reverse(
            'logout'), reverse('register')]:
        next_action = request.GET.get('next')\
            or request.POST.get('next')\
            or '/'
    return next_action
