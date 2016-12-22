from pytest_factoryboy import register

from adhocracy4.test import factories
from tests.actions import factories as actions_factories
from tests.documents import factories as document_factories
from tests.follows import factories as follow_factories
from tests.ideas import factories as idea_fatories
from tests.ratings import factories as rating_factories

register(rating_factories.RatingFactory)
register(actions_factories.CommentFactory)
register(idea_fatories.IdeaFactory)
register(document_factories.DocumentFactory)
register(document_factories.ParagraphFactory)
register(factories.PhaseFactory)
register(follow_factories.FollowFactory)
