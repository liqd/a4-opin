import factory
from tests.factories import ContentTypeFactory, UserFactory


class RateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'euth_rates.Rate'

    value = factory.Faker('random_digit')
    object_pk = factory.Faker('random_digit')
    content_type = factory.SubFactory(ContentTypeFactory)
    user = factory.SubFactory(UserFactory)
