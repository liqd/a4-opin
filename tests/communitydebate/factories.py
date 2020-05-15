import factory

from adhocracy4.test.factories import ModuleFactory
from euth.communitydebate import models as communitydebate_models
from tests.factories import UserFactory


class TopicFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = communitydebate_models.Topic

    name = factory.Faker('name')
    description = '<script>alert("hello");</script>Description'
    creator = factory.SubFactory(UserFactory)
    module = factory.SubFactory(ModuleFactory)


class TopicFileUploadFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = communitydebate_models.TopicFileUpload

    title = factory.Faker('word')
    document = factory.django.FileField(
        filename=factory.Faker('file_name', extension='pdf'),
        data='test')
    topic = factory.SubFactory(TopicFactory)
