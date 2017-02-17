from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.template import Context
from django.views import generic
from rules.contrib import views as rules_views

from euth.dashboard.views import DashboardBaseMixin
from . import forms as forms
from .calculations import BlueprintSuggester


class SuggestFormView(DashboardBaseMixin,
                      rules_views.PermissionRequiredMixin,
                      generic.FormView):
    template_name = 'euth_blueprintsuggest/form.html'
    form_class = forms.GetSuggestionForm
    permission_required = 'euth_organisations.initiate_project'

    def get_success_url(self):
        return reverse('blueprintsuggest-results',
                       kwargs={'organisation_slug': self.organisation.slug})

    def form_valid(self, form):
        suggester = BlueprintSuggester(form.cleaned_data)
        context = {
            'blueprints': suggester.get_blueprints(),
            'request': self.request
        }
        context.update(self.get_context_data())
        context = Context(context)
        return render(self.request, 'euth_blueprintsuggest/result.html',
                      context)

    def get_permission_object(self):
        return self.organisation
