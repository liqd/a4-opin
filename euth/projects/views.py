from django.views.generic import detail, list

from . import models


class ProjectListView(list.ListView):
    model = models.Project

    @property
    def project(self):
        return self.object


class ProjectDetailView(detail.DetailView):
    model = models.Project
