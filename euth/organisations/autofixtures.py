from .models import Organisation
from autofixture import register, AutoFixture
from faker import Faker
from .. import generators


class OrganisationAutoFixture(AutoFixture):

    field_values = {
        'name': generators.FakeOrganisationNameGenerator(),
        'slug': generators.FakeSlugGenerator(),
    }

register(Organisation, OrganisationAutoFixture)
