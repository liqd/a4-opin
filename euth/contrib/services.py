from euth.comments.models import Comment


def deleteComments(contenttype, pk):
    comments = Comment.objects.all().filter(
        content_type=contenttype, object_pk=pk)
    for comment in comments:
        comment.delete()
