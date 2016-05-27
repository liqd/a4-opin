from rest_framework import viewsets
from django_comments.models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    #permission_classes = [IsAccountAdminOrReadOnly]