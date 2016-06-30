import factory
from tests.factories import UserFactory


class OrganisationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'euth_organisations.Organisation'

    name = factory.Faker('name')
    slug = factory.Faker('slug')
    description_why = factory.Faker('text')
    description_how = factory.Faker('text')
    description = factory.Faker('text')

    @factory.post_generation
    def initiators(self, create, extracted, **kwargs):
        if not create:
            user = UserFactory()
            self.initiators.add(user)
            return

        if extracted:
            for user in extracted:
                self.initiators.add(user)
