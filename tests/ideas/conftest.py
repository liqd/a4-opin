from pytest_factoryboy import register

from tests.actions import factories as comment_factories
from tests.ideas import factories as idea_fatories
from tests.ratings import factories as rating_factories

register(rating_factories.RatingFactory)
register(comment_factories.CommentFactory)
register(idea_fatories.IdeaFactory)
