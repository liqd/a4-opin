from django.db.models.signals import post_delete
from django.db.models.signals import post_init
from django.db.models.signals import post_save
from django.dispatch import receiver

from adhocracy4.images import services

from .models import Organisation


@receiver(post_init, sender=Organisation)
def backup_image_path(sender, instance, **kwargs):
    instance._current_image_file = instance.image
    instance._current_logo_file = instance.logo


@receiver(post_save, sender=Organisation)
def delete_old_image(sender, instance, **kwargs):
    old_images = []
    if hasattr(instance, '_current_image_file'):
        if instance._current_image_file != instance.image:
            old_images.append(instance._current_image_file)
    if hasattr(instance, '_current_logo_file'):
        if instance._current_logo_file != instance.logo:
            old_images.append(instance._current_logo_file)
    services.delete_images(old_images)


@receiver(post_delete, sender=Organisation)
def delete_images_for_organisation(sender, instance, **kwargs):
    services.delete_images([instance.image, instance.logo])
