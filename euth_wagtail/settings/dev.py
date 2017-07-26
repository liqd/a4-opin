from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

for template_engine in TEMPLATES:
    template_engine['OPTIONS']['debug'] = True

    ALLOWED_HOSTS = [
    'localhost',
    '192.168.1.56',
    '192.168.1.98',
    '192.168.0.37',
    '192.168.2.115'
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b*1ljsb!x7@d_o$sohx-&q-7n*#r=lwhy542zxk(e=fj%ey3xp'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    import debug_toolbar
except ImportError:
    pass
else:
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE_CLASSES += ['debug_toolbar.middleware.DebugToolbarMiddleware']

    INTERNAL_IPS = ('127.0.0.1', 'localhost')

ADHOCRACY_SDK = "http://localhost:6551/static/js/AdhocracySDK.js"
ADHOCRACY_URL = "http://localhost:6551"

try:
    from .local import *
except ImportError:
    pass
