import factory
from django.contrib.contenttypes.models import ContentType
from tests.factories import UserFactory

class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'comments.Comment'

    comment = factory.Faker('text')
    object_pk = factory.Faker('random_digit_not_null')
    content_type = ContentType.objects.all().first()
    user = factory.SubFactory(UserFactory)
