from pytest_factoryboy import register
from tests.comments import factories as comment_factories
from tests.rates import factories as rates_factories

register(rates_factories.RateFactory)
register(comment_factories.CommentFactory)
