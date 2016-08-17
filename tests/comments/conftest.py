from pytest_factoryboy import register
from tests.rates import factories as rate_factories

import factories

register(rate_factories.RateFactory)
register(factories.CommentFactory)
