import factory

from euth.projects import models

from .. import factories as user_factories
from ..organisations import factories as org_factories


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Project

    name = factory.Faker('name')
    slug = factory.Faker('slug')
    organisation = factory.SubFactory(org_factories.OrganisationFactory)
    description = factory.Faker('text')
    information = factory.Faker('paragraphs')
    is_public = True
    is_draft = False

    @factory.post_generation
    def moderators(self, create, extracted, **kwargs):
        if not extracted:
            user = user_factories.UserFactory()
            self.moderators.add(user)
            return

        if extracted:
            for user in extracted:
                self.moderators.add(user)
