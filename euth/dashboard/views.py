from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from django.views import generic
from rules.compat import access_mixins as mixins

from euth.projects import models as project_models
from euth.user_management import models as user_models

from . import forms

from . import forms


class DashboardProfileView(mixins.LoginRequiredMixin,
                           SuccessMessageMixin,
                           generic.UpdateView):

    model = user_models.User
    template_name = "euth_dashboard/profile_detail.html"
    form_class = forms.ProfileForm
    success_message = _("Your profile was successfully updated")

    def get_object(self):
        return get_object_or_404(user_models.User, pk=self.request.user.id)

    def get_success_url(self):
        return self.request.path


class DashboardProjectListView(mixins.LoginRequiredMixin, generic.ListView):
    model = project_models.Project
    template_name = 'euth_dashboard/project_list.html'

    def get_queryset(self):
        return self.model.objects.filter(
            organisation__initiators=self.request.user
        )

    def get_success_url(self):
        return reverse('dashboard-project-list')


class DashboardProjectUpdateView(mixins.LoginRequiredMixin,
                                 generic.UpdateView):
    model = project_models.Project
    form_class = forms.ExtendedProjectForm
    template_name = 'euth_dashboard/project_form.html'


class DashboardOverviewView(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = "euth_dashboard/dashboard_overview.html"
