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

        try:
            weight = self.request.GET.get('phase')
            phase = project.phases.filter(weight=weight).first()
        except ValueError:
            phase = None

        if phase:
            return phase.view.as_view()
        if project.active_phase:
            return project.active_phase.view.as_view()
        elif project.past_phases:
            return project.past_phases[0].view.as_view()
        else:
            return super().dispatch


class ProjectPhaseMixin(generic.base.ContextMixin):
    def dispatch(self, *args, **kwargs):
        self.project = kwargs['project']

        try:
            weight = self.request.GET.get('phase')
            phase = self.project.phases.filter(weight=weight).first()
        except ValueError:
            phase = None

        if phase:
            self.phase = phase
        elif self.project.active_phase:
            self.phase = self.project.active_phase
        else:
            self.phase = self.project.past_phases[0]

        return super(ProjectPhaseMixin, self).dispatch(*args, **kwargs)
