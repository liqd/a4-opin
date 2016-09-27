from .dev import *

INSTALLED_APPS += [
    'tests.apps.blog.apps.BlogConfig',
    'tests.apps.fakeprojects.apps.FakeProjectsConfig'

]

ACCOUNT_EMAIL_VERIFICATION = 'optional'
