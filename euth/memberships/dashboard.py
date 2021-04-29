from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from adhocracy4.dashboard import DashboardComponent
from adhocracy4.dashboard import components

from . import views


class MembershipRequestComponent(DashboardComponent):
    identifier = 'members'
    weight = 10
    label = _('Members')

    def is_effective(self, project_or_module):
        return project_or_module.is_private or project_or_module.is_semipublic

    def get_base_url(self, project):
        return reverse('a4dashboard:members', kwargs={
            'project_slug': project.slug
        })

    def get_urls(self):
        return [
            (r'^members/project/(?P<project_slug>[-\w_]+)/$',
             views.MembershipsDashboardView.as_view(component=self),
             'members'),
        ]


class MembershipInvitesComponent(DashboardComponent):
    identifier = 'invites'
    weight = 10
    label = _('Invited Members')

    def is_effective(self, project_or_module):
        return project_or_module.is_private or project_or_module.is_semipublic

    def get_base_url(self, project):
        return reverse('a4dashboard:invites', kwargs={
            'project_slug': project.slug
        })

    def get_urls(self):
        return [
            (r'^invites/project/(?P<project_slug>[-\w_]+)/$',
             views.InviteDashboardView.as_view(component=self),
             'invites'),
        ]


components.register_project(MembershipRequestComponent())
components.register_project(MembershipInvitesComponent())
