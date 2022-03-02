from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^(?P<organisation_slug>[-\w_]+)/$',
            views.SuggestFormView.as_view(), name='blueprints-form'),
]
