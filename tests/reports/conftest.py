from pytest_factoryboy import register

from tests.apps.fakeprojects import factories as fprojects_factories
from tests.comments import factories as comment_factories
from tests.reports import factories

register(fprojects_factories.FakeProjectContentFactory)
register(comment_factories.CommentFactory)
register(factories.ReportFactory)
