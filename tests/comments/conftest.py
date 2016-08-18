from pytest_factoryboy import register
from tests.rates import factories as rate_factories

import factories as comment_factories

register(rate_factories.RateFactory)
register(comment_factories.CommentFactory)
