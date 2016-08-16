from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'profile/$',
        views.DashboardProfileView.as_view(), name='dashboard-profile'),
    url(r'',
        views.DashboardOverviewView.as_view(), name='dashboard-overview'),
]
