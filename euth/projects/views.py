from django.views import generic

from . import mixins, models


class ProjectDetailView(mixins.PhaseDispatchMixin,
                        generic.DetailView):


    model = models.Project

    @property
    def project(self):
        """
        Emulate ProjectMixin interface for template sharing.
        """
        return self.get_object()
