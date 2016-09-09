import factory
from tests.factories import UserFactory

from euth.documents import models as document_models

from ..modules.factories import ModuleFactory


class DocumentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = document_models.Document

    name = factory.Faker('name')
    creator = factory.SubFactory(UserFactory)
    module = factory.SubFactory(ModuleFactory)


class ParagraphFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = document_models.Paragraph

    name = factory.Faker('name')
    text = '<script>alert("hello");</script>text'
    weight = factory.Faker('random_number')
    document = factory.SubFactory(DocumentFactory)
