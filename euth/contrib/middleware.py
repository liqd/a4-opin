import pytz
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin


class TimezoneMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.user.is_authenticated and request.user.timezone:
            timezone.activate(pytz.timezone(request.user.timezone))
        else:
            timezone.deactivate()
