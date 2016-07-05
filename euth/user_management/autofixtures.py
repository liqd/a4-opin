from autofixture import register, AutoFixture
from .. import generators
from .models import User



class UserAutoFixture(AutoFixture):

    field_values = {
        'username': generators.FakeNameGenerator(),
    }

register(User, UserAutoFixture)
