from django.views import generic
from rules.contrib.views import PermissionRequiredMixin

from euth.projects import mixins as prj_mixins

from . import models


class DocumentCreateView(
    prj_mixins.ProjectPhaseMixin,
    generic.TemplateView
):
    template_name = 'euth_documents/document_form.html'

    @property
    def document(self):
        return models.Document.objects.filter(module=self.module).first()


class DocumentDetailView(generic.DetailView, prj_mixins.ProjectPhaseMixin):
    model = models.Document

    def get_object(self):
        return models.Document.objects.filter(module=self.module).first()


class ParagraphDetailView(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'euth_documents.view_paragraph'
    model = models.Paragraph

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated
