from django.views import generic

from euth.projects import mixins

from . import models


class DocumentDetailView(generic.DetailView, mixins.ProjectMixin):
    model = models.Document

    def get_object(self):
        return models.Document.objects.filter(module=self.module).first()


class ParagraphDetailView(generic.DetailView):
    model = models.Paragraph
