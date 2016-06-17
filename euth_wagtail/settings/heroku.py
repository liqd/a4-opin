import os
from urllib.parse import urlparse, unquote
from .base import *

mail_url = urlparse(os.environ['MAIL_URL'])
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = mail_url.hostname
EMAIL_PORT = mail_url.port or 587
EMAIL_HOST_USER = unquote(mail_url.username)
EMAIL_HOST_PASSWORD = mail_url.password
DEFAULT_FROM_EMAIL = unquote(mail_url.username)

db_url = urlparse(os.environ['DATABASE_URL'])
if db_url.scheme == 'postgres':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
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
