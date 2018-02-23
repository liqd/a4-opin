from django.views import generic

from euth.projects import mixins as prj_mixins

from . import models as offlinephase_models


class OfflinephaseView(
    prj_mixins.ProjectPhaseMixin,
    generic.DetailView
):
    model = offlinephase_models.Offlinephase

    def get_object(self):
        return self.phase.offlinephase
