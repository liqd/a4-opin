from django.views import generic

from adhocracy4.projects.models import Project


class ProjectListView(generic.ListView):
    model = Project
    paginate_by = 12

    def get_queryset(self):
        return super().get_queryset().filter(is_draft=False)
