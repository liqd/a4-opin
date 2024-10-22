import factory
import pytest
from django.urls import reverse
from pytest_factoryboy import register
from rest_framework.test import APIClient

from adhocracy4.test import helpers

from . import factories

register(factories.UserFactory)
register(factories.UserFactory, 'user2')
register(factories.AdminFactory, 'admin')
register(factories.ContentTypeFactory)


def pytest_configure(config):
    # Patch email background_task decorators for all tests
    helpers.patch_background_task_decorator('adhocracy4.emails.tasks')


@pytest.fixture
def apiclient():
    return APIClient()


@pytest.fixture
def smallImage():
    return factory.django.ImageField(width=200, height=200)


@pytest.fixture
def bigImage():
    return factory.django.ImageField(width=1400, height=1400)


@pytest.fixture
def ImageBMP():
    return factory.django.ImageField(width=1400, height=1400, format='BMP')


@pytest.fixture
def ImagePNG():
    return factory.django.ImageField(width=1400, height=1400, format='PNG')


@pytest.fixture
def image_factory():
    return factories.ImageFactory()


@pytest.fixture
def login_url():
    return reverse('account_login')


@pytest.fixture
def logout_url():
    return reverse('account_logout')


@pytest.fixture
def signup_url():
    return reverse('account_signup')
