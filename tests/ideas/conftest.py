from pytest_factoryboy import register
from tests.comments import factories as comment_factories
from tests.ideas import factories as idea_fatories
from tests.rates import factories as rate_factories

register(rate_factories.RateFactory)
register(comment_factories.CommentFactory)
register(idea_fatories.IdeaFactory)
