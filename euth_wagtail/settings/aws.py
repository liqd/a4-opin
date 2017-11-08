from os import environ

from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

INSTALLED_APPS += [
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
]

ALLOWED_HOSTS = [
    'localhost',
    '{}-{}.eu.platfrom.sh'.format(
        environ['PLATFORM_ENVIRONMENT'],
        environ['PLATFORM_PROJECT']
    ),
]

SECRET_KEY = environ['PLATFORM_PROJECT_ENTROPY']
