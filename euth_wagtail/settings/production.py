from .base import *

COMPRESS = True
COMPRESS_OFFLINE = True

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

INSTALLED_APPS += [
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
]
