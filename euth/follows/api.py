from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, permissions, viewsets

from euth.contrib.api.mixins import AllowPUTAsCreateMixin

from . import models
from .serializers import FollowSerializer


class FollowViewSet(AllowPUTAsCreateMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):

    lookup_field = 'project__slug'
    queryset = models.Follow.objects
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('enabled', )

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)
