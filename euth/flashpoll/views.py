from django.conf import settings
from django.utils.translation import get_language
from django.views import generic

from adhocracy4.projects import mixins

from . import models


class FlashpollDetailView(mixins.ProjectMixin, generic.DetailView):
    model = models.Flashpoll

    def get_object(self, queryset=None):
        return models.Flashpoll.objects.filter(module=self.module).first()

    def get_context_data(self, **kwargs):
        context = {
            'url': '{base_url}/{language}/poll/{poll_id}'.format(
                base_url=settings.FLASHPOLL_URL,
                language=get_language(),
                poll_id=self.get_object().key
            )
        }
        return super().get_context_data(**context)
