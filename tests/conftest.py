import factory
import pytest
from dateutil.parser import parse
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
register(prj_factories.ProjectFactory, 'active_project')
register(mod_factories.ModuleFactory)
register(mod_factories.ModuleFactory, 'active_module')
register(ph_factories.PhaseFactory)
register(member_factories.RequestFactory, 'membership_request')
register(
    ph_factories.PhaseFactory, 'active_phase',
    start_date=parse('2013-01-02 00:00:00 UTC'),
    end_date=parse('2013-01-03 00:00:00 UTC')
)


@pytest.fixture
def membership_request__creator(user2):
    return user2


@pytest.fixture
def active_module__project(active_project):
    return active_project


@pytest.fixture
def active_phase__module(active_module):
    return active_module


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
