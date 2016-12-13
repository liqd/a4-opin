from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_delete
from django.dispatch import receiver

from adhocracy4.ratings import services as rating_services
from euth.contrib import services

from .models import Comment


@receiver(post_delete, sender=Comment)
def delete_comments_for_Comment(sender, instance, **kwargs):
    contenttype = ContentType.objects.get_for_model(instance)
    pk = instance.pk
    services.delete_comments(contenttype, pk)


@receiver(post_delete, sender=Comment)
def delete_ratings_for_Comment(sender, instance, **kwargs):
    contenttype = ContentType.objects.get_for_model(instance)
    pk = instance.pk
    rating_services.delete_ratings(contenttype, pk)
