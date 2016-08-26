from django.views import generic


class PhaseDispatchMixin(generic.DetailView):
    def dispatch(self, request, *args, **kwargs):
        kwargs['project'] = self.get_object()
        return self._view_by_phase()(request, *args, **kwargs)

    def _view_by_phase(self):
        """
        Choose the appropriate view for the current active phase.
        """
        project = self.get_object()

        if project.active_phase:
            return project.active_phase.view.as_view()
        else:
            return super().dispatch


class ProjectMixin(generic.base.ContextMixin):
    def dispatch(self, *args, **kwargs):
        self.project = kwargs['project']
        self.phase = self.project.active_phase
        self.module = self.phase.module if self.phase else None

        self.comment_enabled = self.phase.has_feature('comment', self.model)
        self.crud_enabled = self.phase.has_feature('crud', self.model)
        self.rate_enabled = self.phase.has_feature('rate', self.model)

        return super(ProjectMixin, self).dispatch(*args, **kwargs)
