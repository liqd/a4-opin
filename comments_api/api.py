from rest_framework import viewsets
from django.contrib.comments.models import Comment


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAccountAdminOrReadOnly]