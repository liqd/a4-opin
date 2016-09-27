from pytest_factoryboy import register
from tests.apps.fakeprojects import factories as fprojects_factories
from tests.ratings import factories as rating_factories

import factories as comment_factories

register(fprojects_factories.FakeProjectContent)
register(rating_factories.RatingFactory)
register(comment_factories.CommentFactory)
