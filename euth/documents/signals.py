from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_delete, post_init, post_save
from django.dispatch import receiver

from euth.contrib import services

from .models import Document, Paragraph

@receiver(post_delete, sender=Document)
def delete_comments_for_Document(sender, instance, **kwargs):
    contenttype = ContentType.objects.get_for_model(instance)
    pk = instance.pk
    services.delete_comments(contenttype, pk)

@receiver(post_delete, sender=Paragraph)
def delete_comments_for_Paragraph(sender, instance, **kwargs):
    contenttype = ContentType.objects.get_for_model(instance)
    pk = instance.pk
    services.delete_comments(contenttype, pk)
