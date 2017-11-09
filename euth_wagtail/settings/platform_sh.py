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


routes = environ.get('PLATFORM_ROUTES')
if routes:
    routes = json.loads(str(base64.b64decode(routes), 'utf-8'))
    app_name = os.getenv('PLATFORM_APPLICATION_NAME')
    for url, route in routes.items():
        host = urlparse(url).netloc;
        if host not in ALLOWED_HOSTS and route['type'] == 'upstream' and route['upstream'] == app_name:
            ALLOWED_HOSTS.append(host)


relationships = environ.get('PLATFORM_RELATIONSHIPS')
if relationships:
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

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = environ.get('PLATFORM_SMTP_HOST')

# FIXME: PLATFORM_PROJECT_ENTROPY should also be available during build
SECRET_KEY = environ.get('PLATFORM_PROJECT_ENTROPY', 'tExb2F2cG3sfnOYlwhV1VqXFFbDfLOxbmfnLOEEy')
