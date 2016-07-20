from django.db.models.signals import post_delete
from django.dispatch import receiver
from easy_thumbnails.files import get_thumbnailer

from .models import Project


@receiver(post_delete, sender=Project)
def delete_images_for_Project(sender, instance, **kwargs):
    thumbnailer = get_thumbnailer(instance.image)
    thumbnailer.delete_thumbnails()
    instance.image.delete(False)
