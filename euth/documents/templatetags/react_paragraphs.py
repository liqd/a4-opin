import json

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import template

from euth.documents.serializers import DocumentSerializer

register = template.Library()


@register.inclusion_tag('euth_documents/react_paragraphs.html',
                        takes_context=True)
def react_paragraphs(context, doc, module):

    serializer = DocumentSerializer(doc)
    document = serializer.data
    widget = CKEditorUploadingWidget(config_name='image-editor')
    widget._set_config()
    config = widget.config

    context = {
        'document': json.dumps(document),
        'module': module.pk,
        'config': json.dumps(config),
    }

    return context
