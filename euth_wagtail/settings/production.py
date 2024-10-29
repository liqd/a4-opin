from .base import *

DEBUG = False

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}

try:
    from .local import *
except ImportError:
    pass

INSTALLED_APPS += [
    # 'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
]

DATA_UPLOAD_MAX_NUMBER_FIELDS = None
