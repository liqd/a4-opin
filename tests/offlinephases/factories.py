import factory

from adhocracy4.test.factories import PhaseFactory
from euth.offlinephases import models as offlinephase_models


class FileUploadFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = offlinephase_models.FileUpload

    phase = factory.SubFactory(PhaseFactory)


class OfflinephaseFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = offlinephase_models.Offlinephase

    document = factory.SubFactory(FileUploadFactory)
