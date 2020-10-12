import math

from django.views import generic
from rules.contrib import views as rules_views

from euth.dashboard.mixins import DashboardBaseMixin

from . import blueprints
from . import forms


def custom_round(x):
    if x % 1 < 0.5:
        return math.floor(x)
    else:
        return math.ceil(x)


def filter_blueprints(aim, result, experience, motivation,
                      participants, scope, duration, accessibility,
                      options=blueprints.blueprints,
                      fallbacks=blueprints.fallbacks):
    candidates = []

    for name, blueprint in options:
        if aim not in blueprint.requirements.aims:
            continue

        requirements = blueprint.requirements

        if result and experience and motivation:

            req_results = requirements.results
            req_experience = requirements.experience
            req_motivation = requirements.motivation

            if req_results and result not in req_results:
                continue
            if req_experience and req_experience.value > experience.value:
                continue
            if req_motivation and req_motivation.value > motivation.value:
                continue

        timeneeded = compute_time_needed(
            blueprint, participants, duration, scope,
            motivation, accessibility, experience)
        candidates.append((name, blueprint, timeneeded))

    if not candidates:
        name = fallbacks[aim]
        blueprint = dict(options)[name]
        timeneeded = compute_time_needed(
            blueprint, participants, duration, scope,
            motivation, accessibility, experience)
        candidates.append((name, blueprint, timeneeded))

    return candidates


def compute_complexity(blueprint, participants, duration, scope):

    return custom_round(sum((
        blueprint.complexity.participants[0] +
        participants.value * blueprint.complexity.participants[1],
        blueprint.complexity.duration[0] +
        duration.value * blueprint.complexity.duration[1],
        blueprint.complexity.scope[0] +
        scope.value * blueprint.complexity.scope[1]
    )))


def compute_mobilisation(motivation, accessibility):
    # modify to match different coding for motivation
    return custom_round((5 - motivation.value + accessibility.value) / 2)


def compute_time_needed(
        blueprint, participants, duration, scope,
        motivation, accessibility, experience
):
    complexity = compute_complexity(blueprint, participants, duration, scope)
    mobilisation = compute_mobilisation(motivation, accessibility)
    # modify to match different coding for experience
    value = (complexity + 1) * (mobilisation + 5 - experience.value)

    if value < 13:
        return 5
    elif value < 21:
        return 10
    elif value < 28:
        return 15
    elif value < 35:
        return 20
    elif value < 40:
        return 25
    elif value < 50:
        return 30
    else:
        return 35


class SuggestFormView(DashboardBaseMixin,
                      rules_views.PermissionRequiredMixin,
                      generic.FormView):
    template_name = 'euth_blueprints/form.html'
    form_class = forms.GetSuggestionForm
    permission_required = 'a4projects.add_project'

    def form_valid(self, form):
        context = {
            'blueprints': filter_blueprints(**form.cleaned_data),
            'organisation': self.organisation,
            'request': self.request  # FIXME: should be done context processor
        }
        context.update(self.get_context_data())
        return self.response_class(
            request=self.request,
            template='euth_blueprints/result.html',
            context=context
        )

    def get_permission_object(self):
        return self.organisation
