import factory
from django.conf import settings
from django.contrib.auth.hashers import make_password


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = settings.AUTH_USER_MODEL

    username = factory.Sequence(lambda n: 'user{}'.format(n))
    password = make_password('password')
    email = factory.Sequence(lambda n: 'user{}@liqd.net'.format(n))


class AdminFactory(UserFactory):
    is_superuser = True
    is_staff = True
