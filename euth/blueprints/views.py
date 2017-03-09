from django.template import Context
from django.views import generic
from rules.contrib import views as rules_views

from euth.dashboard.views import DashboardBaseMixin

from . import blueprints, forms


def filter_blueprints(aim, result, experience, motivation,
                      options=blueprints.blueprints):
    candidates = []

    for name, blueprint in options:
        if aim not in blueprint.requirements.aims:
            continue

        requirements = blueprint.requirements

        if result and experience and motivation:
            if result not in requirements.results:
                continue
            if requirements.experience.value > experience.value:
                continue
            if requirements.motivation.value > motivation.value:
                continue
        candidates.append((name, blueprint))

    if not candidates:
        candidates.append(blueprints.get_fallback_blueprint(aim))

    return candidates


class SuggestFormView(DashboardBaseMixin,
                      rules_views.PermissionRequiredMixin,
                      generic.FormView):
    template_name = 'euth_blueprints/form.html'
    form_class = forms.GetSuggestionForm
    permission_required = 'euth_organisations.initiate_project'

    def form_valid(self, form):
        context = {
            'blueprints': filter_blueprints(**form.cleaned_data),
            'organisation': self.organisation,
            'request': self.request  # FIXME: should be done context processor
        }
        context.update(self.get_context_data())
        context = Context(context)
        return self.response_class(
            request=self.request,
            template='euth_blueprints/result.html',
            context=context
        )

    def get_permission_object(self):
        return self.organisation
