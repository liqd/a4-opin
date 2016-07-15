from django.core import exceptions

from euth.phases import models as phases_models
from . import models


class ProjectMixin():

    def dispatch(self, *args, **kwargs):
        if 'project' not in kwargs:
            msg = '{} `project` kwarg required'.format(self.__cls__.__name__)
            raise exceptions.ImproperlyConfigured(msg)

        self.project = models.Project.objects.get(slug=kwargs['project'])
        self.phase = phases_models.Phase.objects.active_phase(self.project)
        self.module = self.phase.module if self.phase else None
        return super(ProjectMixin, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectMixin, self).get_context_data(*args, **kwargs)
        context['project'] = self.project
        context['phase'] = self.phase
        context['module'] = self.module
        return context
