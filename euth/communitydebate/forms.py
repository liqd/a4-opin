from django import forms

from adhocracy4.categories import forms as category_forms
from euth.contrib import widgets
from euth.contrib.mixins import ImageRightOfUseMixin

from . import models


class TopicForm(category_forms.CategorizableFieldMixin,
                ImageRightOfUseMixin,
                forms.ModelForm):

    class Meta:
        model = models.Topic
        fields = ['name', 'description', 'image', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = '---'

    class Media:
        js = ('fileupload_formset.js',)


class TopicFileUploadForm(forms.ModelForm):

    class Meta:
        model = models.TopicFileUpload
        fields = ['title', 'document']
        widgets = {
            'document': widgets.FileUploadWidget()
        }


TopicFileUploadFormset = forms.inlineformset_factory(models.Topic,
                                                     models.TopicFileUpload,
                                                     TopicFileUploadForm,
                                                     extra=1, max_num=3,
                                                     can_delete=True)
