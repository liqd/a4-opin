from adhocracy4 import phases

from . import apps, views


class FakePhase0(phases.PhaseContent):
    app = apps.FakeProjectsConfig.label
    phase = 'phase'
    view = views.FakePhase0View
    weight = 10


class FakePhase1(phases.PhaseContent):
    app = apps.FakeProjectsConfig.label
    phase = 'phase'
    view = views.FakePhase1View
    weight = 20


phases.content.register(FakePhase0())
phases.content.register(FakePhase1())
