from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views import generic

from adhocracy4.projects import mixins
from adhocracy4.projects.models import Project


class ProjectPhaseMixin(generic.base.ContextMixin):
    """Add project, module and phase attributes to the view and the template.

    This is a counterpart to the Phase- / ModuleDispatcher logic and a slight
    modification of the `adhocracy4.projects.mixins.ProjectMixin`.

    To consider the object context from get_object() set the
    get_context_from_object attribute. Enable this only if get_object() does
    not access the project, module and phase properties.

    In addition to the functionality from core an optional `phase` parameter
    can be given to a `project_slug` url. This parameter will select a phase
    from within the project by weight. Since weights are not guaranteed to be
    unique with in a project, this is not a universal approach. It only works
    in OPIN because there is always only one module per project.

    As a difference from core module kwargs, slug or get_object context are not
    supported. The are either not needed in OPIN and not easily implementable
    without infinit recursion.

    Designed to be used in item-(list, form or detail) view.

    """
    project_lookup_field = 'slug'
    project_url_kwarg = 'project_slug'
    module_lookup_field = 'slug'
    module_url_kwarg = 'module_slug'
    get_context_from_object = False

    @property
    def phase(self):
        try:
            weight = self.request.GET.get('phase')
            phase = self.project.phases.filter(weight=weight).first()
        except ValueError:
            phase = None

        if phase:
            return phase
        else:
            return self.project.last_active_phase

    @property
    def module(self):
        """Get the module from the current phase."""
        if self.phase:
            return self.phase.module

    @property
    def project(self):
        """Get the project from the kwargs, url or current object."""
        if self.get_context_from_object:
            return self._get_object(Project, 'project')

        if 'project' in self.kwargs \
                and isinstance(self.kwargs['project'], Project):
            return self.kwargs['project']

        if self.project_url_kwarg and self.project_url_kwarg in self.kwargs:
            lookup = {
                self.project_lookup_field: self.kwargs[self.project_url_kwarg]
            }
            return get_object_or_404(Project, **lookup)

    def _get_object(self, cls, attr):
        # CreateView supplies a defect get_object method and has to be excluded
        if hasattr(self, 'get_object') \
                and not isinstance(self, generic.CreateView):
            try:
                object = self.get_object()
                if isinstance(object, cls):
                    return object

                if hasattr(object, attr):
                    return getattr(object, attr)
            except Http404:
                return None
            except AttributeError:
                return None

        return None


class PhaseDispatchMixin(
        ProjectPhaseMixin,
        mixins.PhaseDispatchMixin
):
    """
    Desgined to be used as mixin in project detail view.
    """

    def _view_by_phase(self):
        """
        Take view from phase property if present.
        """
        if self.phase:
            return self.phase.view.as_view()
        else:
            return super()._view_by_phase()
