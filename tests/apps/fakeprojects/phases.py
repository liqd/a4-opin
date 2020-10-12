from adhocracy4 import phases

from . import apps
from . import views


class FakePhase0(phases.PhaseContent):
    app = apps.FakeProjectsConfig.label
    phase = 'phase0'
    view = views.FakePhase0View


class FakePhase1(phases.PhaseContent):
    app = apps.FakeProjectsConfig.label
    phase = 'phase1'
    view = views.FakePhase1View


phases.content.register(FakePhase0())
phases.content.register(FakePhase1())
