from .base import *

DEBUG = False

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

try:
    from .local import *
except ImportError:
    pass

INSTALLED_APPS += [
    # 'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
]

DATA_UPLOAD_MAX_NUMBER_FIELDS = None
