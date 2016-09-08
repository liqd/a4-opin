from pytest_factoryboy import register
from tests.comments import factories as comment_factories
from tests.ratings import factories as ratings_factories

register(ratings_factories.RatingFactory)
register(comment_factories.CommentFactory)
