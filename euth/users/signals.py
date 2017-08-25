from django.db.models import signals
from django.dispatch import receiver

from adhocracy4.images import services

from . import models


@receiver(signals.post_init, sender=models.User)
def backup_image_path(sender, instance, **kwargs):
    if instance.avatar:
        instance._current_image_file = instance.avatar


@receiver(signals.post_save, sender=models.User)
def delete_old_image(sender, instance, **kwargs):
    if hasattr(instance, '_current_image_file'):
        if instance._current_image_file != instance.avatar:
            services.delete_images([instance._current_image_file])


@receiver(signals.post_delete, sender=models.User)
def delete_images_for_User(sender, instance, **kwargs):
    services.delete_images([instance._avatar])
