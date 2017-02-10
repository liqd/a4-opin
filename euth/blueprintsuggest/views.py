from django.views import generic

from . import forms as forms


class SuggestFormView(generic.FormView):
    template_name = 'euth_blueprintsuggest/form.html'
    form_class = forms.GetSuggestionForm
