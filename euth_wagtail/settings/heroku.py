import os
from urllib.parse import unquote
from urllib.parse import urlparse

from .base import *

mail_url = urlparse(os.environ['MAIL_URL'])
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = 1 if mail_url.scheme == "smtps" else 0
EMAIL_HOST = mail_url.hostname
EMAIL_PORT = mail_url.port or 587
EMAIL_HOST_USER = unquote(mail_url.username)
EMAIL_HOST_PASSWORD = mail_url.password
DEFAULT_FROM_EMAIL = unquote(mail_url.username)

db_url = urlparse(os.environ['DATABASE_URL'])
if db_url.scheme == 'postgres':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': unquote(db_url.path.strip('/')),
            'USER': unquote(db_url.username),
            'PASSWORD': unquote(db_url.password),
            'HOST': db_url.hostname,
            'PORT': db_url.port or 5432,
        }
    }

ALLOWED_HOSTS = [
    'localhost',
    'opin-dev.liqd.de',
    'opin-dev.herokuapp.com',
]

SECRET_KEY = os.environ['SECRET_KEY']

ADHOCRACY_URL = 'https://a3-opin-stage.liqd.net/'
ADHOCRACY_SDK = 'https://a3-opin-stage.liqd.net/static/js/AdhocracySDK.js'

SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

COMPRESS = True
COMPRESS_OFFLINE = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + [
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
SECURE_SSL_REDIRECT = True
