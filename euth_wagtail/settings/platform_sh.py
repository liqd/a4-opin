import base64
import json
from os import environ
from urllib.parse import urlparse

from .production import *

try:
    from .local import *
except ImportError:
    pass


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

def get_platfrom_environ(name):
    if name in environ:
        return json.loads(str(base64.b64decode(environ[name]), 'utf-8'))


routes = get_platfrom_environ('PLATFORM_ROUTES')
if routes:
    app_name = os.getenv('PLATFORM_APPLICATION_NAME')
    for url, route in routes.items():
        host = urlparse(url).netloc;
        if host not in ALLOWED_HOSTS and route['type'] == 'upstream' and route['upstream'] == app_name:
            ALLOWED_HOSTS.append(host)


relationships = get_platfrom_environ('PLATFORM_RELATIONSHIPS')
if relationships:
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

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST=environ.get('PLATFORM_SMTP_HOST')

variables = get_platfrom_environ('PLATFORM_VARIABLES')
SECRET_KEY = variables['DJANGO_SECRET_KEY']
