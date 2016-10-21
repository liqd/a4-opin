from rest_framework import viewsets

from euth.contrib.api.permissions import IsModerator

from .models import Document
from .serializers import DocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = (
        IsModerator,
    )
