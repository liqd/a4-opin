import factory

from django.contrib.auth.hashers import make_password


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'auth.User'

    username = factory.Faker('name')
    password = make_password('password')


class AdminFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'auth.User'

    username = factory.Faker('name')
    password = make_password('password')
    is_superuser = True


class ContentTypeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'contenttypes.ContentType'

    app_label = factory.Faker('name')
    model = factory.Faker('name')
    name = factory.Faker('name')
