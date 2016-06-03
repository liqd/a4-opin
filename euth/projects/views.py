from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from . import models


class ProjectListView(ListView):
    model = models.Project


class ProjectDetailView(DetailView):
    model = models.Project
