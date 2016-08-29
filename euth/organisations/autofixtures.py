from autofixture import AutoFixture, generators, register
from faker import Factory

from .models import Organisation, OrganisationTranslation

fake = Factory.create()


class OrganisationAutoFixture(AutoFixture):

    IMAGESIZES = ((1300, 600),)
    LOGOSIZES = ((400, 400),)

    field_values = {
        'name': generators.CallableGenerator(fake.company),
        'slug': generators.CallableGenerator(fake.slug),
        'image': generators.ImageGenerator(sizes=IMAGESIZES),
        'logo': generators.ImageGenerator(sizes=LOGOSIZES),
        'facebook_handle': 'LIQDeV',
        'twitter_handle': 'bunnybuddhism',
        'instragram_handle': 'insta.plane',
        'webpage': 'https://example.com',
    }


class OrganisationTranslationsAutoFixture(AutoFixture):

    field_values = {
        'title': generators.CallableGenerator(fake.company),
        'description_why': generators.CallableGenerator(fake.text),
        'description_how': generators.CallableGenerator(fake.text),
        'description': generators.CallableGenerator(fake.text),
        'language_code': 'en',
    }

    follow_fk = True


register(Organisation, OrganisationAutoFixture)
register(OrganisationTranslation, OrganisationTranslationsAutoFixture)
