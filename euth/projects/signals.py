from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import Project


@receiver(post_delete, sender=Project)
def delete_images_for_Project(sender, instance, **kwargs):
    instance.image.delete(False)
