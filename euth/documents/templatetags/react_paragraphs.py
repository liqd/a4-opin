from ckeditor.widgets import CKEditorWidget
from django import template
from rest_framework.renderers import JSONRenderer

from euth.documents.serializers import DocumentSerializer

register = template.Library()


@register.inclusion_tag('euth_documents/react_paragraphs.html',
                        takes_context=True)
def react_paragraphs(context, doc, module):

    serializer = DocumentSerializer(doc)
    document = JSONRenderer().render(serializer.data)
    widget = CKEditorWidget()
    config = widget.config

    context = {
        'document': document,
        'module': module.pk,
        'config': config
    }

    return context
