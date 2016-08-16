from django.views import generic


class DashboardProfileView(generic.TemplateView):

    template_name = "euth_dashboard/profile_detail.html"


class DashboardOverviewView(generic.TemplateView):

    template_name = "euth_dashboard/dashboard_overview.html"
