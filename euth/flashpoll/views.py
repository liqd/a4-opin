import json
import requests
from django.conf import settings
from django.utils.translation import get_language
from django.views import generic
from requests.auth import HTTPBasicAuth

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
        context['pollid'] = self.get_object().key
        context['module_settings'] = "euth_flashpoll"    

        url_poll = '{base_url}/poll/{poll_id}'.format(
            base_url=settings.FLASHPOLL_BACK_URL,
            poll_id=context['pollid']
        )

        headers = {'Content-type': 'application/json'}
        res = requests.get(url_poll,
                        headers=headers,
                        auth=HTTPBasicAuth(settings.FLASHPOLL_BACK_USER,
                                            settings.FLASHPOLL_BACK_PASSWORD
                                            ))
        context['poll'] = json.loads(res.text)

        url_poll = '{base_url}/poll/{poll_id}/result'.format(
            base_url=settings.FLASHPOLL_BACK_URL,
            poll_id=context['pollid']
        )

        headers = {'Content-type': 'application/json'}
        res = requests.get(url_poll,
                        headers=headers,
                        auth=HTTPBasicAuth(settings.FLASHPOLL_BACK_USER,
                                            settings.FLASHPOLL_BACK_PASSWORD
                                            ))
        context['pollresult'] = json.loads(res.text)

        return super().get_context_data(**context)
