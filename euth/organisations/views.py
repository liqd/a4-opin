from django.views import generic

from . import models


class OrganisationDetailView(generic.DetailView):
    model = models.Organisation

    def visible_projects(self):
        projects = self.object.project_set.order_by('-created')
        if self.request.user in self.object.initiators.all():
            return projects.all()
        else:
            return projects.filter(is_draft=False)


class OrganisationListView(generic.ListView):
    model = models.Organisation
    paginate_by = 12
