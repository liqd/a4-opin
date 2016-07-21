from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_delete
from django.dispatch import receiver

from euth.contrib import services

from .models import Idea


@receiver(post_delete, sender=Idea)
def delete_images_for_Idea(sender, instance, **kwargs):
    instance.image.delete(False)


@receiver(post_delete, sender=Idea)
def delete_comments_for_Idea(sender, instance, **kwargs):
    contenttype = ContentType.objects.get_for_model(instance)
    pk = instance.pk
    services.deleteComments(contenttype, pk)
