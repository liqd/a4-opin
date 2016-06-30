from django.shortcuts import render
from django.views import generic

from . import models

class OrganisationDetailView(generic.DetailView):
    model = models.Organisation
