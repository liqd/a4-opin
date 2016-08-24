from braces.views import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from django.views import generic

from euth.user_management import models as user_models


class DashboardProfileView(LoginRequiredMixin,
                           SuccessMessageMixin,
                           generic.UpdateView):

    model = user_models.User
    template_name = "euth_dashboard/profile_detail.html"
    fields = ['avatar', 'email']
    success_message = _("Your profile was successfully updated")

    def get_object(self):
        return get_object_or_404(user_models.User, pk=self.request.user.id)

    def get_success_url(self):
        return self.request.path


class DashboardOverviewView(LoginRequiredMixin, generic.TemplateView):

    template_name = "euth_dashboard/dashboard_overview.html"
