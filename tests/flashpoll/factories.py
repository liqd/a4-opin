import factory

from euth.flashpoll import models as flashpoll_models

from ..modules.factories import ModuleFactory


class FlashpollFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = flashpoll_models.Flashpoll

    module = factory.SubFactory(ModuleFactory)
    key = factory.Faker('pystr', min_chars=20, max_chars=30)
