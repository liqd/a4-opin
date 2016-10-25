from rest_framework import filters, permissions, viewsets
from rest_framework.response import Response

from euth.contrib.api.permissions import IsUserOrReadOnly

from .models import Comment
from .serializers import ThreadSerializer


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all().order_by('-created')
    serializer_class = ThreadSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('object_pk', 'content_type')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        comment = self.get_object()
        if self.request.user == comment.user:
            comment.is_removed = True
        if self.request.user.is_superuser:
            comment.is_censored = True
        comment.save()
        serializer = self.get_serializer(comment)
        return Response(serializer.data)
