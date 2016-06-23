from .dev import *


wagtail_deps =  [ 'taggit', 'modelcluster' ]
our_wagtail_apps = [ 'home', 'search', 'projects',  ]
INSTALLED_APPS = [ app for app in INSTALLED_APPS
                   if not 'wagtail.' in app and app not in our_wagtail_apps + wagtail_deps ]
