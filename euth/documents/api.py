from rest_framework import status, viewsets
from rest_framework.response import Response

from euth.contrib.api.permissions import IsModerator

from .models import Document
from .serializers import DocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def create(self, request):
        """
        Sets the user of the request as user of the document
        """
        serializer = DocumentSerializer(
            data=request.data,
            context={'request': request})

        if serializer.is_valid():
            document = serializer.create(serializer.validated_data)
            return Response(DocumentSerializer(document).data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (
        IsModerator,
    )
