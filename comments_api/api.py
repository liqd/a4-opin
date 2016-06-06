from django.utils import timezone
from django_comments.models import Comment

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
        is_public=True, is_removed=False).order_by('-submit_date')
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('object_pk', 'content_type', 'user_name')

    def create(self, request):

        data = {
            'comment': request.data['comment'],
            'object_pk': request.data['object_pk'],
            'content_type': request.data['content_type'],
            'site': 1,
            'is_public': True,
            'is_removed': False,
            'submit_date': timezone.now(),
            'user_name': request.user,
        }

        serializer = CommentSerializer(data=data)

        if serializer.is_valid():
            obj = serializer.save()
            obj.user = request.user
            obj.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
