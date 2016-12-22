from pytest_factoryboy import register

from tests.follows import factories as follow_factories
from tests.ideas import factories as ideas_factories

register(follow_factories.FollowFactory)
register(ideas_factories.IdeaFactory)
