import base64
import json
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

if environ.get('PLATFORM_ENVIRONMENT'):
    run_time = True
else:
    run_time = False
build_time = not run_time


ALLOWED_HOSTS = [
    'localhost',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] [%(levelname)s] %(module)s -- %(message)s',
            'datefmt' : '%Y-%m-%d %H:%M:%S %z',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        }
    },
    'loggers': {
                'django': {
                    'handlers': ['console'],
                    'propagate': True,
                }
    }
}

if run_time:
    ALLOWED_HOSTS.append(
        '{}-{}.eu.platfrom.sh'.format(
            environ['PLATFORM_ENVIRONMENT'],
            environ['PLATFORM_PROJECT']
        )
    )

    relationships = os.environ['PLATFORM_RELATIONSHIPS']
    relationships = json.loads(str(base64.b64decode(relationships), 'utf-8'))
    db_settings = relationships['database'][0]

    DATABASES = {
        "default": {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': db_settings['path'],
            'USER': db_settings['username'],
            'PASSWORD': db_settings['password'],
            'HOST': db_settings['host'],
            'PORT': db_settings['port'],
        }
    }

# FIXME: PLATFORM_PROJECT_ENTROPY should also be available during build
SECRET_KEY = environ.get('PLATFORM_PROJECT_ENTROPY', 'tExb2F2cG3sfnOYlwhV1VqXFFbDfLOxbmfnLOEEy')
