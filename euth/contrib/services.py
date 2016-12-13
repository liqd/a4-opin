from easy_thumbnails.files import get_thumbnailer

from euth.comments.models import Comment


def delete_comments(contenttype, pk):
    comments = Comment.objects.all().filter(
        content_type=contenttype, object_pk=pk)
    for comment in comments:
        comment.delete()


def delete_images(imagefields):
    for imagefield in imagefields:
        thumbnailer = get_thumbnailer(imagefield)
        thumbnailer.delete_thumbnails()
        if imagefield.name:
            imagefield.storage.delete(imagefield.name)
