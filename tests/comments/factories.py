import factory
from django.contrib.contenttypes.models import ContentType
from tests.factories import UserFactory
from tests.factories import ContentTypeFactory

class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'comments.Comment'

    comment = factory.Faker('text')
    object_pk = factory.Faker('random_digit_not_null')
    content_type = factory.SubFactory(ContentTypeFactory)
    user = factory.SubFactory(UserFactory)
