from autofixture import AutoFixture, generators, register
from faker import Factory

from .models import Module

fake = Factory.create()


class ModuleAutoFixture(AutoFixture):

    field_values = {
        'name': generators.CallableGenerator(fake.company),
        'description': generators.CallableGenerator(fake.text)
    }

register(Module, ModuleAutoFixture)
