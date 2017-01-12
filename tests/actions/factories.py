import factory

from tests.apps.fakeprojects import factories
from tests.factories import UserFactory


class CommentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'a4comments.Comment'

    comment = factory.Faker('text')
    content_object = factory.SubFactory(factories.FakeProjectContentFactory)
    creator = factory.SubFactory(UserFactory)
