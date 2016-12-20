from pytest_factoryboy import register
from tests.comments import factories as comment_factories
from tests.documents import factories as document_fatories

register(comment_factories.CommentFactory)
register(document_fatories.DocumentFactory)
register(document_fatories.ParagraphFactory)
