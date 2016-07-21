import os

from django.conf import settings
from easy_thumbnails.files import get_thumbnailer


def createThumbnail(imagefield):
    thumbnailer = get_thumbnailer(imagefield)
    thumbnail = thumbnailer.generate_thumbnail(
        {'size': (800, 400), 'crop': 'smart'})
    thumbnailer.save_thumbnail(thumbnail)
    thumbnail_path = os.path.join(settings.MEDIA_ROOT, thumbnail.path)
    return thumbnail_path
