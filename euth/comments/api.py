from django.utils import timezone
from .models import Comment

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .serializers import CommentSerializer
from .permissions import IsUserOrReadOnly
from rest_framework import filters


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all().filter(
        is_removed=False).order_by('-submit_date')
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('object_pk', 'content_type', 'user')

    def create(self, request):

        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            obj = serializer.save(user=self.request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
