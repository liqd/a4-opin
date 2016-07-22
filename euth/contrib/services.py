from easy_thumbnails.files import get_thumbnailer

from euth.comments.models import Comment


def delete_comments(contenttype, pk):
    comments = Comment.objects.all().filter(
        content_type=contenttype, object_pk=pk)
    for comment in comments:
        comment.delete()


def delete_images(imagefields):
    for image in imagefields:
        thumbnailer = get_thumbnailer(image)
        thumbnailer.delete_thumbnails()
        image.delete(False)
