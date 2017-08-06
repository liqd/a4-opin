from adhocracy4.categories import forms as category_forms

from . import models


class IdeaForm(category_forms.CategorizableForm):
    class Meta:
        model = models.Idea
        fields = ['name', 'description', 'image', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = '---'
