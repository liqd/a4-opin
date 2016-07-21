from django.db.models.signals import post_delete
from django.dispatch import receiver
from easy_thumbnails.files import get_thumbnailer

from .models import Organisation


@receiver(post_delete, sender=Organisation)
def delete_images_for_organisation(sender, instance, **kwargs):
    services.delete_images([instance.image, instance.logo])
