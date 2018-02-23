from django.db.models.signals import post_delete, post_init, post_save
from django.dispatch import receiver

from .models import FileUpload


@receiver(post_init, sender=FileUpload)
def backup_file_path(sender, instance, **kwargs):
    instance._current_document_file = instance.document


@receiver(post_save, sender=FileUpload)
def delete_old_fileuploads(sender, instance, **kwargs):
    if hasattr(instance, '_current_document_file'):
        if instance._current_document_file != instance.document:
            instance._current_document_file.delete(False)


@receiver(post_delete, sender=FileUpload)
def delete_documents_for_Fileupload(sender, instance, **kwargs):
    instance.document.delete(False)
