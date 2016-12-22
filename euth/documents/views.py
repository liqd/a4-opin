from django.views import generic
from rules.contrib.views import PermissionRequiredMixin

from adhocracy4.projects import mixins

from . import models


class DocumentCreateView(mixins.ProjectMixin, generic.TemplateView):
    template_name = 'euth_documents/document_form.html'

    @property
    def document(self):
        return models.Document.objects.filter(module=self.module).first()


class DocumentDetailView(generic.DetailView, mixins.ProjectMixin):
    model = models.Document

    def get_object(self):
        return models.Document.objects.filter(module=self.module).first()


class ParagraphDetailView(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'euth_documents.view_paragraph'
    model = models.Paragraph

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()
