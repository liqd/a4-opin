import factory
from django.contrib.contenttypes.models import ContentType
from tests.factories import UserFactory


def get_comments_contenttype():
    return ContentType.objects.get(app_label="comments", model="comment")


class ReportFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'euth_reports.Report'

    description = factory.Faker('text')
    content_type = get_comments_contenttype()
    user = factory.SubFactory(UserFactory)
