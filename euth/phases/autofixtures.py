from autofixture import AutoFixture, generators, register
from faker import Factory

from . import content
from .models import Phase

fake = Factory.create()


class PhaseAutoFixture(AutoFixture):

    field_values = {
        'name': generators.CallableGenerator(fake.company),
        'type': generators.ChoicesGenerator(choices=content.as_choices()),
    }

    follow_pk = True

register(Phase, PhaseAutoFixture)
