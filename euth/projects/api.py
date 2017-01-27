from rest_framework import viewsets

from adhocracy4.projects.models import Project

from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = (permissions.IsAuthenticated,)
