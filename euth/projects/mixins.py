from django.core import exceptions
from django.views import generic

from euth.phases import models as phases_models

from . import models


class ProjectMixin(generic.base.ContextMixin):

    def dispatch(self, *args, **kwargs):
        if 'project' not in kwargs:
            msg = '{} `project` kwarg required'.format(self.__cls__.__name__)
            raise exceptions.ImproperlyConfigured(msg)

        self.project = models.Project.objects.get(slug=kwargs['project'])
        self.phase = phases_models.Phase.objects.active_phase(self.project)
        self.module = self.phase.module if self.phase else None
        return super(ProjectMixin, self).dispatch(*args, **kwargs)
