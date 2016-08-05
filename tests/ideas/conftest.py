from pytest_factoryboy import register
from tests.comments import factories as comment_factories
from tests.ideas import factories as idea_fatories
from tests.modules import factories as module_factories
from tests.organisations import factories as organisation_factories
from tests.projects import factories as project_factories
from tests.rates import factories as rate_factories

register(rate_factories.RateFactory)
register(comment_factories.CommentFactory)
register(organisation_factories.OrganisationFactory)
register(project_factories.ProjectFactory)
register(module_factories.ModuleFactory)
register(idea_fatories.IdeaFactory)
