from django.contrib.auth import mixins
from django.shortcuts import get_object_or_404
from django.utils import functional
from django.views import generic

from adhocracy4.projects import models as project_models
from euth.organisations import models as org_models


class DashboardBaseMixin(mixins.LoginRequiredMixin,
                         generic.base.ContextMixin,):

    @functional.cached_property
    def user_has_organisation(self):
        return bool(self.request.user.organisation_set.all())

    @functional.cached_property
    def organisation(self):
        if 'organisation_slug' in self.kwargs:
            slug = self.kwargs['organisation_slug']
            return get_object_or_404(org_models.Organisation, slug=slug)
        if 'project_slug' in self.kwargs:
            slug = self.kwargs['project_slug']
            project = get_object_or_404(project_models.Project, slug=slug)
            return project.organisation
        else:
            return self.request.user.organisation_set.first()

    @functional.cached_property
    def other_organisations_of_user(self):
        user = self.request.user
        if self.organisation:
            return user.organisation_set.exclude(pk=self.organisation.pk)
        else:
            return None

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated
