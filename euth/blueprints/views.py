from django.template import Context
from django.views import generic
from rules.contrib import views as rules_views

from euth.dashboard.views import DashboardBaseMixin

from . import blueprints, forms


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
            if result not in requirements.results:
                continue
            if requirements.experience.value > experience.value:
                continue
            if requirements.motivation.value > motivation.value:
                continue

        timeneeded = compute_time_needed(blueprint, participants,
            duration, scope, motivation, accessibility, experience)
        candidates.append((name, blueprint, timeneeded))

    if not candidates:
        name = fallbacks[aim]
        candidates.append((name, dict(options)[name]))

    return candidates


def compute_complexity(blueprint, participants, duration, scope):
    return sum((
        blueprints.complexity.participants[0] +
        participants.value * blueprints.complexity.participants[1],
        blueprints.complexity.duration[0] +
        duration.value * blueprints.complexity.duration[1],
        blueprints.complexity.scope[0] +
        scope.value * blueprints.complexity.scope[1],
    ))


def compute_mobilisation(motivation, accessibility):
    return (motivation.value + accessibility.value)/2


def compute_time_needed(
        blueprint, participants, duration, scope,
        motivation, accessibility, experience
):

    complexity = compute_complexity(blueprint, participants, duration, scope)
    mobilisation = compute_mobilisation(motivation, accessibility)

    inverse_experience = 5 - experience.value
    value = (complexity + 1) * (mobilisation + inverse_experience)

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
        context = Context(context)
        return self.response_class(
            request=self.request,
            template='euth_blueprints/result.html',
            context=context
        )

    def get_permission_object(self):
        return self.organisation
