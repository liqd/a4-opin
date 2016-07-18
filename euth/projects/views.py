from django.views.generic import detail, list

from . import models


class ProjectListView(list.ListView):
    model = models.Project


class ProjectDetailView(detail.DetailView):
    model = models.Project
