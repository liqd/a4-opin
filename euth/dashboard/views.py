from braces.views import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views import generic

from euth.user_management import models as user_models


class DashboardProfileView(LoginRequiredMixin, generic.UpdateView):

    model = user_models.User
    template_name = "euth_dashboard/profile_detail.html"
    fields = ['avatar', 'email']

    def get_object(self):
        return get_object_or_404(user_models.User, pk=self.request.user.id)

    def get_success_url(self):
        return self.request.path


class DashboardOverviewView(LoginRequiredMixin, generic.TemplateView):

    template_name = "euth_dashboard/dashboard_overview.html"
