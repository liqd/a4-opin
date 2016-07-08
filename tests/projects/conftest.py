from tests.organisations import factories as org_factories
from tests.projects import factories

from pytest_factoryboy import register

register(org_factories.OrganisationFactory)
register(factories.ProjectFactory)
