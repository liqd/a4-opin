import factory
import pytest
from pytest_factoryboy import register

from tests.actions import factories as comment_factories
from tests.communitydebate import factories as communitydebate_fatories
from tests.ratings import factories as rating_factories

register(rating_factories.RatingFactory)
register(comment_factories.CommentFactory)
register(communitydebate_fatories.TopicFactory)
register(communitydebate_fatories.TopicFileUploadFactory)


@pytest.fixture
def DocumentCSV():
    return factory.django.FileField(filename='example_doc.csv')
