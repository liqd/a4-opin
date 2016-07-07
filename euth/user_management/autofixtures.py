from autofixture import generators, register, AutoFixture
from faker import Factory

from .models import User

fake = Factory.create()


class UserAutoFixture(AutoFixture):

    field_values = {
        'username': generators.CallableGenerator(fake.name)
    }

register(User, UserAutoFixture)
