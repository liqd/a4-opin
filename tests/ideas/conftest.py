from pytest_factoryboy import register
from tests.ideas import factories as idea_fatories
from tests.modules import factories as module_factories
from tests.organisations import factories as organisation_factories
from tests.projects import factories as project_factories

register(organisation_factories.OrganisationFactory)
register(project_factories.ProjectFactory)
register(module_factories.ModuleFactory)
register(idea_fatories.IdeaFactory)
