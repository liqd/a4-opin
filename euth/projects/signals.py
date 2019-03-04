from django.db.models.signals import post_delete
from django.dispatch import receiver

from adhocracy4.projects.models import Project

from .emails import DeleteProjectEmail


@receiver(post_delete, sender=Project)
def send_delete_project_notification(sender, instance, **kwargs):
    DeleteProjectEmail.send_no_object(instance)
