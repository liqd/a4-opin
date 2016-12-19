import factory

from euth.ideas import models as idea_models
from tests.factories import UserFactory

from ..modules.factories import ModuleFactory


class IdeaFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = idea_models.Idea

    name = factory.Faker('name')
    description = '<script>alert("hello");</script>Description'
    creator = factory.SubFactory(UserFactory)
    module = factory.SubFactory(ModuleFactory)
