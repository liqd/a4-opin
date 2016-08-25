from django.views.generic import detail

from euth.phases import models as phases_models

from . import models


class ProjectDetailView(detail.DetailView):
    model = models.Project

    @property
    def project(self):
        """ Emulate ProjectMixin interface for template sharing. """
        return self.object

project_detail_view = ProjectDetailView.as_view()


def dispatch_project_view(*args, **kwargs):
    project = models.Project.objects.get(slug=kwargs['slug'])
    active_phase = phases_models.Phase.objects.active_phase(project)

    if active_phase:
        kwargs['project'] = kwargs['slug']
        view = active_phase.view.as_view()
    else:
        view = project_detail_view

    return view(*args, **kwargs)
