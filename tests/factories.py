import factory

from django.contrib.auth.hashers import make_password


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'auth.User'

    username = factory.Faker('name')
    password = make_password('password')
    email = factory.Faker('email')
