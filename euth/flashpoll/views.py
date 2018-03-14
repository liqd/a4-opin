import json
import uuid

import requests
from django.conf import settings
from django.utils.translation import get_language
from django.views import generic
from requests.auth import HTTPBasicAuth

from adhocracy4.dashboard import mixins
from adhocracy4.projects.mixins import ProjectMixin
from euth.projects import mixins as prj_mixins

from . import models


class FlashpollLoadMixin:

    def get_context_data(self, **kwargs):
        useremail = str(uuid.uuid4())
        if not self.request.user.is_anonymous():
            useremail = self.request.user.email

        context = {
            'url': '{base_url}/{language}/poll/{poll_id}?userId={mail}'.format(
                base_url=settings.FLASHPOLL_URL,
                language=get_language(),
                poll_id=self.get_object().key,
                mail=useremail
            )
        }
        context['pollid'] = self.get_object().key
        context['module_settings'] = "euth_flashpoll"

        if self.get_object().key:
            url_poll = '{base_url}/poll/{poll_id}'.format(
                base_url=settings.FLASHPOLL_BACK_URL,
                poll_id=context['pollid']
            )

            headers = {'Content-type': 'application/json'}
            res = requests.get(
                url_poll,
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
            res = requests.get(
                url_poll,
                headers=headers,
                auth=HTTPBasicAuth(
                    settings.FLASHPOLL_BACK_USER,
                    settings.FLASHPOLL_BACK_PASSWORD
                ))
            context['pollresult'] = json.loads(res.text)

        return super().get_context_data(**context)


class FlashpollDetailView(prj_mixins.ProjectPhaseMixin,
                          FlashpollLoadMixin,
                          generic.DetailView):
    model = models.Flashpoll

    def get_object(self, queryset=None):
        return models.Flashpoll.objects.filter(module=self.module).first()


class FlashpollExportView(ProjectMixin,
                          mixins.DashboardBaseMixin,
                          mixins.DashboardComponentMixin,
                          generic.DetailView
                          ):

    model = models.Flashpoll
    permission_required = 'a4projects.change_project'
    template_name = 'euth_flashpoll/flashpoll_export.html'

    def get_permission_object(self):
        return self.project

    def get_object(self, queryset=None):
        return models.Flashpoll.objects.filter(module=self.module).first()

    def get_context_data(self, **kwargs):
        useremail = str(uuid.uuid4())
        if not self.request.user.is_anonymous():
            useremail = self.request.user.email

            url = '{base_url}/{language}/poll/{poll_id}?userId={mail}'.format(
                base_url=settings.FLASHPOLL_URL,
                language=get_language(),
                poll_id=self.get_object().key,
                mail=useremail
            )

        context = dict(url=url)
        context['pollid'] = self.get_object().key
        context['module_settings'] = "euth_flashpoll"

        if self.get_object().key:

            url_poll = '{base_url}/poll/{poll_id}'.format(
                base_url=settings.FLASHPOLL_BACK_URL,
                poll_id=context['pollid']
            )

            headers = {'Content-type': 'application/json'}
            res = requests.get(
                url_poll,
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
            res = requests.get(
                url_poll,
                headers=headers,
                auth=HTTPBasicAuth(
                    settings.FLASHPOLL_BACK_USER,
                    settings.FLASHPOLL_BACK_PASSWORD
                ))
            context['pollresult'] = json.loads(res.text)

            url_poll = '{base_url}/poll/{poll_id}/results'.format(
                base_url=settings.FLASHPOLL_BACK_URL,
                poll_id=context['pollid']
            )

            headers = {'Content-type': 'application/json'}
            res = requests.get(url_poll,
                               headers=headers,
                               auth=HTTPBasicAuth(
                                    settings.FLASHPOLL_BACK_USER,
                                    settings.FLASHPOLL_BACK_PASSWORD
                                ))
            context['pollresults'] = json.loads(res.text)

        return super().get_context_data(**context)
