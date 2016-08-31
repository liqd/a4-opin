from django.views import generic

from . import models


class ProjectMixin(generic.base.ContextMixin):

    def dispatch(self, *args, **kwargs):
        self.project = models.Project.objects.get(slug=kwargs['project'])
        self.phase = self.project.active_phase
        self.module = self.phase.module if self.phase else None

        self.comment_enabled = self.phase.has_feature('comment', self.model)
        self.crud_enabled = self.phase.has_feature('crud', self.model)
        self.rate_enabled = self.phase.has_feature('rate', self.model)

        return super(ProjectMixin, self).dispatch(*args, **kwargs)
