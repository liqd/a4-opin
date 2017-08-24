from django.views.generic import list

from tests.apps.blog import models


class FakePhase0View(list.ListView):
    model = models.Post
    template_name = 'fakephase0'


class FakePhase1View(list.ListView):
    model = models.Post
    template_name = 'fakephase1'
