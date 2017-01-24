from django.views import generic

from . import models


class OrganisationDetailView(generic.DetailView):
    model = models.Organisation

    def visible_projects(self):
        if self.request.user in self.object.initiators.all():
            return self.object.project_set.all()
        else:
            return self.object.project_set.filter(is_draft=False)


class OrganisationListView(generic.ListView):
    model = models.Organisation
    paginate_by = 12
