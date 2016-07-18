import factory
import random

from euth.modules import models
from ..projects import factories as project_factories


class ModuleFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Module

    name = factory.Faker('name')
    slug = factory.Faker('slug')
    description = factory.Faker('text')
    weight = random.randint(1, 1000)
    project = factory.SubFactory(project_factories.ProjectFactory)
