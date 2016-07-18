from rest_framework import filters, permissions, status, viewsets
from rest_framework.response import Response

from .models import Comment
from .permissions import IsUserOrReadOnly
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all().order_by('-created')
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('object_pk', 'content_type', 'user')

    def create(self, request):
        """
        Sets the user of the request as user of the comment
        """
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Checks if current user is the user of the comment
        or if the user is admin and sets the flags accordingly.
        NOTE: Comment is NOT deleted.
        """
        comment = self.get_object()

        serializer = CommentSerializer(comment, {}, partial=True)

        if serializer.is_valid():
            obj = serializer.save()
            if request.user == comment.user:
                obj.is_removed = True
            if request.user.is_superuser:
                obj.is_censored = True
            obj.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
