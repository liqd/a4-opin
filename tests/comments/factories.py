import factory
from django.contrib.contenttypes.models import ContentType

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'comments.Comment'

    comment = comment,
    object_pk = object_pk,
    content_type = ContentType.objects.all().first(),
    user = user = factory.SubFactory(UserFactory)
