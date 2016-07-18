from pytest_factoryboy import register
from tests.organisations import factories as org_factories
from tests.projects import factories

register(org_factories.OrganisationFactory)
register(factories.ProjectFactory)
