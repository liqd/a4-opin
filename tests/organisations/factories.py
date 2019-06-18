import factory

from tests.factories import UserFactory


class OrganisationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'euth_organisations.Organisation'

    name = factory.Faker('company')
    slug = factory.Sequence(lambda n: 'organisation%d' % n)
    description_why = factory.Faker('text')
    description_how = factory.Faker('text')
    description = factory.Faker('text')
    country = factory.Faker('country_code')
    place = factory.Faker('city')

    @factory.post_generation
    def initiators(self, create, extracted, **kwargs):
        if not extracted:
            user = UserFactory()
            self.initiators.add(user)
            return

        if extracted:
            for user in extracted:
                self.initiators.add(user)
