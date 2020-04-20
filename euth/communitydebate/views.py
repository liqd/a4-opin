from django.views import generic

from . import models as communitydebate_models


class TopicListView(generic.ListView):
    model = communitydebate_models.Topic

    def get_queryset(self):
        return communitydebate_models.Topic.objects.all()


class TopicDetailView(generic.DetailView):
    model = communitydebate_models.Topic
    template_name = 'euth_communitydebate/topic_detail.html'
