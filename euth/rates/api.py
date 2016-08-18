from rest_framework import filters, mixins, permissions, status, viewsets
from rest_framework.response import Response

from .models import Rate
from .permissions import IsUserOrReadOnly
from .serializers import RateSerializer


class RateViewSet(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):

    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('object_pk', 'content_type', 'user', 'value')

    def create(self, request):
        """
        Sets the user of the request as user of the rate
        """
        serializer = RateSerializer(
            data=request.data,
            context={'request': request}
        )

        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Sets value to zero
        NOTE: Rate is NOT deleted.
        """
        rate = self.get_object()

        serializer = RateSerializer(
            rate,
            {},
            partial=True,
            context={'request': request}
        )

        if serializer.is_valid():
            obj = serializer.save()
            obj.value = 0
            obj.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
