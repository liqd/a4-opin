import factory
from tests.factories import UserFactory


class ReportFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'euth_reports.Report'

    description = factory.Faker('text')
    user = factory.SubFactory(UserFactory)
