import factory

from django.conf import settings
from django.contrib.auth.hashers import make_password


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = settings.AUTH_USER_MODEL

    username = factory.Faker('name')
    password = make_password('password')
    email = factory.Faker('email')


class AdminFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = settings.AUTH_USER_MODEL

    username = factory.Faker('name')
    password = make_password('password')
    is_superuser = True


class ContentTypeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'contenttypes.ContentType'

    app_label = factory.Faker('name')
    model = factory.Faker('name')
    name = factory.Faker('name')
