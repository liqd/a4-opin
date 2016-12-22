from .dev import *

INSTALLED_APPS += [
    'tests.apps.blog.apps.BlogConfig',
    'tests.apps.fakeprojects.apps.FakeProjectsConfig'

]

A4_ORGANISATION_FACTORY = 'tests.organisations.factories.OrganisationFactory'
A4_USER_FACTORY = 'tests.factories.UserFactory'

ACCOUNT_EMAIL_VERIFICATION = 'optional'
