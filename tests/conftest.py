import pytest
from django.urls import reverse
from pytest_factoryboy import register

from . import factories

register(factories.UserFactory)
register(factories.UserFactory, 'user2')
register(factories.AdminFactory, 'admin')


@pytest.fixture
def login_url():
    return reverse('account_login')


@pytest.fixture
def logout_url():
    return reverse('account_logout')


@pytest.fixture
def signup_url():
    return reverse('account_signup')
