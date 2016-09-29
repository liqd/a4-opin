from django.utils.translation import get_language
from django.views import generic

from euth.projects import mixins

from . import models


class FlashpollDetailView(mixins.ProjectMixin, generic.DetailView):
    model = models.Flashpoll

    def get_object(self, queryset=None):
        return models.Flashpoll.objects.first()

    def get_context_data(self, **kwargs):
        context = {
            'url': 'http://flashpoll.opin.me/{}/poll/{}'.format(
                get_language(),
                kwargs['object'].key
            )
        }
        return super().get_context_data(**context)
