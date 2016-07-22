from pytest_factoryboy import register
from tests.modules import factories as mod_factories
from tests.organisations import factories as org_factories
from tests.phases import factories
from tests.projects import factories as prj_factories

register(org_factories.OrganisationFactory)
register(prj_factories.ProjectFactory)
register(mod_factories.ModuleFactory)
register(factories.PhaseFactory)
