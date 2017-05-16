from rest_framework import permissions, viewsets

from adhocracy4.projects.models import Project
from euth.contrib.api.permissions import IsInitiatorOrSuperUser
from euth.users.models import User

from . import emails
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated, IsInitiatorOrSuperUser)

    def perform_update(self, serializer):
        moderators = serializer.instance.moderators.values_list('id',
                                                                flat=True)
        # create a set from current moderators and moderators after ajax
        moderators = set(moderators)
        post_moderators = set(serializer.initial_data['moderators'])
        new_moderator = post_moderators - moderators
        if len(new_moderator) == 1:
            new_moderator = User.objects.get(id__exact=new_moderator.pop())
            emails.ModeratorAddedEmail.send(
                serializer.instance,
                user=new_moderator
            )

        serializer.save()
