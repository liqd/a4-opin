import factory

from adhocracy4.test.factories import ModuleFactory
from euth.flashpoll import models as flashpoll_models


class FlashpollFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = flashpoll_models.Flashpoll

    module = factory.SubFactory(ModuleFactory)
    key = factory.Faker('pystr', min_chars=20, max_chars=30)
