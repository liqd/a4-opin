from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import Organisation


@receiver(post_delete, sender=Organisation)
def delete_images_for_Organusation(sender, instance, **kwargs):
    instance.image.delete(False)
    instance.logo.delete(False)
