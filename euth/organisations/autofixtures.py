from autofixture import AutoFixture, generators, register
from faker import Factory

from .models import Organisation

fake = Factory.create()


class OrganisationAutoFixture(AutoFixture):

    IMAGESIZES = ((1300, 600),)
    LOGOSIZES = ((400, 400),)

    field_values = {
        'name': generators.CallableGenerator(fake.company),
        'slug': generators.CallableGenerator(fake.slug),
        'image': generators.ImageGenerator(sizes=IMAGESIZES),
        'logo': generators.ImageGenerator(sizes=LOGOSIZES)
    }

register(Organisation, OrganisationAutoFixture)
