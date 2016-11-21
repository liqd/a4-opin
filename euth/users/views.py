from django.views.generic.detail import DetailView
from euth.projects.models import Project
from . import models


class ProfileView(DetailView):
    model = models.User
    slug_field = 'username'

    @property
    def get_participated_projects(self):
        return Project.objects.filter(participants=self.object)
