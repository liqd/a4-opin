from django.db import models as django_models
from django.utils import timezone
from django.views.generic.detail import DetailView
from euth.projects.models import Project
from . import models


class ProfileView(DetailView):
    model = models.User
    slug_field = 'username'

    @property
    def get_participated_projects(self):
        user = self.object

        qs = Project.objects.filter(
            django_models.Q(
                module__phase__end_date__gt=timezone.now()
            ),  # only active projects
            django_models.Q(follow__creator=user) |
            django_models.Q(participants=user) |
            django_models.Q(moderators=user)
        ).distinct()

        return qs
