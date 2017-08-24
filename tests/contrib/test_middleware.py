import pytest
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.utils import timezone

from euth.contrib.middleware import TimezoneMiddleware


@pytest.mark.django_db
def test_request_processed_user(rf, user):
    request = rf.get('/')
    request.user = user
    TimezoneMiddleware().process_request(request)
    assert user.timezone == timezone.get_current_timezone_name()


@pytest.mark.django_db
def test_request_processed_default(rf):
    request = rf.get('/')
    user = AnonymousUser()
    request.user = user
    TimezoneMiddleware().process_request(request)
    assert settings.TIME_ZONE == timezone.get_current_timezone_name()
