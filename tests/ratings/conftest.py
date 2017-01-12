from pytest_factoryboy import register

from tests.actions import factories as comment_factories
from tests.apps.fakeprojects import factories as fprojects_factories
from tests.ratings import factories as ratings_factories

register(fprojects_factories.FakeProjectContentFactory)
register(ratings_factories.RatingFactory)
register(comment_factories.CommentFactory)
