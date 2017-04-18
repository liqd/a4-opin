from django.views import generic

from euth.contrib import filters

from . import models



class OrganisationDetailView(generic.DetailView):
    model = models.Organisation
    filter = filters.ArchivedFilter

    def visible_projects(self):
        projects = self.object.project_set.order_by('-created')
        if self.request.user in self.object.initiators.all():
            return projects.all()
        else:
            if 'is_archived' in self.request.GET and \
                    self.request.GET['is_archived'] == 'true':
                filter_archived = True
            else:
                filter_archived = False

            return projects.filter(
                        is_draft=False,
                        is_archived=filter_archived
                    )


class OrganisationListView(generic.ListView):
    model = models.Organisation
    paginate_by = 12
