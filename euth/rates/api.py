from rest_framework import filters, mixins, permissions, viewsets
from rest_framework.response import Response

from .models import Rate
from .permissions import IsUserOrReadOnly
from .serializers import RateSerializer


class RateViewSet(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):

    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('object_pk', 'content_type')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, pk=None):
        """
        Sets value to zero
        NOTE: Rate is NOT deleted.
        """
        rate = self.get_object()
        rate.value = 0
        rate.save()
        serializer = self.get_serializer(rate)
        return Response(serializer.data)
