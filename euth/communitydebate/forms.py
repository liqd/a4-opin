from django import forms

from adhocracy4.categories import forms as category_forms

from . import models


class TopicForm(category_forms.CategorizableFieldMixin, forms.ModelForm):
    class Meta:
        model = models.Topic
        fields = ['name', 'description', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = '---'
