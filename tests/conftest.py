import factory
import pytest
from django.core.urlresolvers import reverse
from pytest_factoryboy import register
from rest_framework.test import APIClient
from tests.memberships import factories as member_factories
from tests.modules import factories as mod_factories
from tests.organisations import factories as org_factories
from tests.phases import factories as ph_factories
from tests.projects import factories as prj_factories

from . import factories

register(factories.UserFactory)
register(factories.UserFactory, 'user2')
register(factories.AdminFactory, 'admin')
register(factories.ContentTypeFactory)

register(org_factories.OrganisationFactory)
register(prj_factories.ProjectFactory)
register(mod_factories.ModuleFactory)
register(ph_factories.PhaseFactory)
register(member_factories.RequestFactory, 'membership_request')
register(member_factories.InviteFactory)


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
