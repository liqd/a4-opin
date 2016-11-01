import factory
from tests.apps.fakeprojects import factories
from tests.factories import UserFactory


class RatingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'euth_ratings.Rating'

    value = factory.Faker('random_digit')
    creator = factory.SubFactory(UserFactory)
    content_object = factory.SubFactory(factories.FakeProjectContentFactory)
