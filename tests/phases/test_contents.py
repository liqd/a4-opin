from tests.apps.blog import models
from tests.apps.blog.phases import BlogPhase

from euth.phases import PhaseContent, content


def test_blogapp_phase_registered():
    assert 'blog:020:phase' in content
    assert content['blog:020:phase'].__class__ is BlogPhase
    assert ('blog:020:phase', 'BlogPhase (blog:phase)') in content.as_choices()


def test_phase_content():
    class DummyPhase(PhaseContent):
        app = 'dummy'
        phase = 'phase'
        weight = 9999

    phase = DummyPhase()

    assert phase.identifier == 'dummy:999:phase'
    assert str(phase) == 'DummyPhase (dummy:phase)'


def test_phase_features():
    class DummyPhase(PhaseContent):
        app = 'dummy'
        phase = 'phase'
        weight = 9999
        features = {
            'comment': (models.Post,)
        }

    phase = DummyPhase()
    assert phase.has_feature('comment', models.Post)
