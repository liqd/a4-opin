import factory

from django.contrib.auth.hashers import make_password


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'auth.User'

    username = factory.Faker('name')
    password =  make_password('password')


class RegistrationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'user_management.Registration'

    username = factory.Faker('name')
    email = factory.Faker('email')
    password = 'password'
    token = factory.Faker('uuid4')
    next_action = factory.Faker('uri_path')