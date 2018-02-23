from django.core.urlresolvers import reverse
from django.views import generic
from rules.contrib.views import PermissionRequiredMixin

from euth.projects import mixins as prj_mixins

from . import models as offlinephase_models
from .forms import OfflinephaseMultiForm


class OfflinephaseView(
    prj_mixins.ProjectPhaseMixin,
    generic.DetailView
):
    model = offlinephase_models.Offlinephase

    def get_object(self):
        return self.phase.offlinephase


class OfflinephaseEditView(PermissionRequiredMixin, generic.UpdateView):
    model = offlinephase_models.Offlinephase
    permission_required = 'euth_offlinephases.modify_offlinephase'
    form_class = OfflinephaseMultiForm

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        qs = offlinephase_models.FileUpload.objects.filter(
            offlinephase=self.object)
        kwargs['fileuploads__queryset'] = qs
        kwargs['offlinephase__instance'] = self.object
        return kwargs

    def get_success_url(self):
        return reverse('offlinephase-edit', args=(self.get_object().pk,))
