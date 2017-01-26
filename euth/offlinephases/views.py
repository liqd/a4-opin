from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.core.urlresolvers import reverse
from django.views import generic
from rules.contrib.views import PermissionRequiredMixin

from adhocracy4.projects import mixins

from . import models as offlinephase_models


class OfflinephaseView(generic.DetailView, mixins.ProjectMixin):
    model = offlinephase_models.Offlinephase

    def get_object(self):
        return self.phase.offlinephase


class OfflinephaseEditView(PermissionRequiredMixin, generic.UpdateView):
    model = offlinephase_models.Offlinephase
    fields = ['text']
    permission_required = 'euth_offlinephases.modify_offlinephase'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

    def get_form(self, form_class):
        form = super().get_form(form_class)
        form.fields['text'].widget = CKEditorUploadingWidget(
            config_name='image-editor')
        return form

    def get_success_url(self):
        project = self.object.project
        organisation = self.object.organisation
        if (project.active_phase and
                self.object.project.active_phase.offlinephase == self.object):
            return reverse('project-detail', args=(project.slug,))
        else:
            return reverse('dashboard-project-edit',
                           args=(organisation.slug, project.slug))
