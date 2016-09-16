from django.views import generic
from rules.contrib.views import PermissionRequiredMixin

from euth.projects import mixins

from . import models


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
