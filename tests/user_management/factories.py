import factory

from ..factories import UserFactory


class RegistrationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'user_management.Registration'

    username = factory.Faker('name')
    email = factory.Faker('email')
    password = 'password'
    token = factory.Faker('uuid4')
    next_action = factory.Faker('uri_path')


class ResetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'user_management.Reset'

    token = factory.Faker('uuid4')
    next_action = factory.Faker('uri_path')
    user = factory.SubFactory(UserFactory)
