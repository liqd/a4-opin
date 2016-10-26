import factory
from tests.apps.fakeprojects import factories
from tests.factories import UserFactory


class ReportFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'euth_reports.Report'

    description = factory.Faker('text')
    creator = factory.SubFactory(UserFactory)
    content_object = factory.SubFactory(factories.FakeProjectContentFactory)
