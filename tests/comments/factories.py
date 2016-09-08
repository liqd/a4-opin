import factory
from tests.factories import ContentTypeFactory, UserFactory


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'euth_comments.Comment'

    comment = factory.Faker('text')
    object_pk = factory.Faker('random_digit_not_null')
    content_type = factory.SubFactory(ContentTypeFactory)
    user = factory.SubFactory(UserFactory)
