import factory
from tests.factories import ContentTypeFactory, UserFactory


class RatingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'euth_ratings.Rating'

    value = factory.Faker('random_digit')
    object_pk = factory.Faker('random_digit')
    content_type = factory.SubFactory(ContentTypeFactory)
    user = factory.SubFactory(UserFactory)
