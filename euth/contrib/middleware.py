import pytz

from django.utils import timezone


class TimezoneMiddleware(object):

    def process_request(self, request):
        if request.user.is_authenticated() and request.user.timezone:
            timezone.activate(pytz.timezone(request.user.timezone))
        else:
            timezone.deactivate()
