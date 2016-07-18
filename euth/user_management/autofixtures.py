from autofixture import AutoFixture, generators, register
from faker import Factory

from .models import User

fake = Factory.create()


class UserAutoFixture(AutoFixture):

    field_values = {
        'username': generators.CallableGenerator(fake.name)
    }

register(User, UserAutoFixture)
