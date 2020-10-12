from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from adhocracy4.dashboard import DashboardComponent
from adhocracy4.dashboard import components

from . import views


class ModeratorsComponent(DashboardComponent):
    identifier = 'moderators'
    weight = 10
    label = _('Moderators')

    def is_effective(self, project_or_module):
        return True

    def get_base_url(self, project):
        return reverse('a4dashboard:moderators', kwargs={
            'project_slug': project.slug
        })

    def get_urls(self):
        return [
            (r'^moderators/project/(?P<project_slug>[-\w_]+)/$',
             views.ModeratorsDashboardView.as_view(component=self),
             'moderators'),
        ]


components.register_project(ModeratorsComponent())
