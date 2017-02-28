import factory

from adhocracy4.test.factories import PhaseFactory
from euth.offlinephases import models as offlinephase_models


class OfflinephaseFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = offlinephase_models.Offlinephase

    text = factory.Faker('text')
    phase = factory.SubFactory(PhaseFactory)
