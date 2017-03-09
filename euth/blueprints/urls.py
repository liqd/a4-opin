from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<organisation_slug>[-\w_]+)/$',
        views.SuggestFormView.as_view(), name='blueprints-form'),
]
