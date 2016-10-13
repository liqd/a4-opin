from django import forms
from django.forms import modelformset_factory
from django.utils.translation import ugettext_lazy as _

from contrib.multiforms import multiform

from . import models


class DocumentCreateForm(forms.ModelForm):

    class Meta:
        model = models.Document
        fields = ['name']
        labels = {
            'name': _('Title'),
        }


class ParagraphCreateForm(forms.ModelForm):

    class Meta:
        model = models.Paragraph
        fields = ['name', 'text']
        labels = {
            'name': _('Headline'),
            'text': _('Paragraph')
        }


class DocumentCreateMultiForm(multiform.MultiModelForm):

    base_forms = [
        ('document', DocumentCreateForm),
        ('paragraphs', modelformset_factory(
            models.Paragraph, ParagraphCreateForm
        )),
    ]

    def __init__(self, document, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.module = kwargs.pop('module')
        if document:
            self.document = document
            paragraphs = self.document.paragraphs_sorted.values()
            kwargs['document__instance'] = self.document
            kwargs['paragraphs__queryset'] = models.Paragraph.objects.none()
            kwargs[
                'paragraphs__initial'] = paragraphs
        super().__init__(*args, **kwargs)

    def update(self, objects, commit):
        document_fields = objects['document']
        self.document.name = document_fields.name
        if commit:
            self.document.save()
            for paragraph in self.document.paragraphs_sorted:
                paragraph.delete()
            self.create_paragraphs(
                objects['paragraphs'], self.document, commit)
            objects['document'] = self.document
        return objects

    def create_paragraphs(self, paragraphs, document, commit):

        for index, paragraph in enumerate(paragraphs):
            paragraph.weight = index
            paragraph.document = document
            if commit:
                paragraph.save()

    def save(self, commit=True):
        objects = super().save(commit=False)

        if hasattr(self, 'document'):
            return self.update(objects, commit)
        else:
            document = objects['document']
            document.creator = self.user
            document.module = self.module
            if commit:
                document.save()

            paragraphs = objects['paragraphs']

            self.create_paragraphs(paragraphs, document, commit)

            return objects
