from autofixture import register, AutoFixture, generators
from faker import Factory

from .models import Organisation

fake = Factory.create()


class OrganisationAutoFixture(AutoFixture):

    field_values = {
        'name': generators.CallableGenerator(fake.company),
        'slug': generators.CallableGenerator(fake.slug),
    }

register(Organisation, OrganisationAutoFixture)
