from django.views import generic

from adhocracy4.modules.models import Module


class PhaseDispatchMixin(generic.DetailView):
    def dispatch(self, request, *args, **kwargs):
        kwargs['project'] = self.get_object()
        phase = self._get_relevant_phase()

        if phase:
            kwargs['module'] = phase.module
            view = phase.view.as_view()
        else:
            view = super().dispatch

        return view(request, *args, **kwargs)

    def _get_relevant_phase(self):
        """
        Choose the relevant phase with in the project.
        """
        project = self.get_object()

        try:
            weight = self.request.GET.get('phase')
            phase = project.phases.filter(weight=weight).first()
        except ValueError:
            phase = None

        if phase:
            return phase
        elif project.last_active_phase:
            return project.last_active_phase


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
        else:
            self.phase = self.project.last_active_phase

        self.module = self.phase.module
        return super(ProjectPhaseMixin, self).dispatch(*args, **kwargs)


class ModuleMixin(generic.base.ContextMixin):

    def dispatch(self, *args, **kwargs):
        mod_slug = kwargs.get('slug')
        self.module = Module.objects.get(slug=mod_slug)
        self.project = self.module.project
        return super().dispatch(*args, **kwargs)
