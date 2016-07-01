import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from . import factories

register(factories.UserFactory)
register(factories.UserFactory, 'user2')
register(factories.AdminFactory, 'admin')
register(factories.ContentTypeFactory)


@pytest.fixture
def apiclient():
    return APIClient()
