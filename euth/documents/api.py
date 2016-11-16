from rest_framework import mixins, permissions, viewsets

from euth.contrib.api.permissions import IsModerator

from .models import Document
from .serializers import DocumentSerializer


class DocumentViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = (
        permissions.IsAuthenticated, IsModerator,
    )
