from pytest_factoryboy import register
from tests.comments import factories as comment_factories
from tests.reports import factories

register(comment_factories.CommentFactory)
register(factories.ReportFactory)
