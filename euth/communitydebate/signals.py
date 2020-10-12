import os

from django.db.models.signals import post_delete
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import TopicFileUpload


@receiver(post_delete, sender=TopicFileUpload)
def delete_topic_file_upload(sender, instance, **kwargs):
    if instance.document:
        instance.document.delete(False)


@receiver(pre_save, sender=TopicFileUpload)
def delete_topic_file_upload_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = sender.objects.get(pk=instance.pk).document
    except sender.DoesNotExist:
        return False

    new_file = instance.document
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
