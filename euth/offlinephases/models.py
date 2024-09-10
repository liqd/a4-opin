def document_path(instance, filename):
    return 'documents/offlineevent_{}/{}'.format(
        instance.offlineevent.pk, filename)
