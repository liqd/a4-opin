from django.views import generic

from adhocracy4.projects import mixins

from . import models as offlinephase_models


class OfflinephaseView(generic.DetailView, mixins.ProjectMixin):
    model = offlinephase_models.Offlinephase

    def get_object(self):
        return self.module.project.active_phase.offlinephase
