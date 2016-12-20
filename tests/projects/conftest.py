from pytest_factoryboy import register
from tests.modules import factories as mod_factories
from tests.organisations import factories as org_factories
from tests.phases import factories as ph_factories
from tests.projects import factories

register(org_factories.OrganisationFactory)
register(factories.ProjectFactory)
register(mod_factories.ModuleFactory)
register(ph_factories.PhaseFactory)
