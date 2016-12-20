import pytest
from tests.apps.blog import models
from tests.apps.blog.phases import BlogPhase

from euth.phases import PhaseContent, content


@pytest.fixture
def dummy_phase():
    class DummyPhase(PhaseContent):
        app = 'dummy'
        phase = 'phase'
        weight = 9999
        features = {
            'comment': (models.Post,)
        }

    return DummyPhase()


def test_blogapp_phase_registered():
    assert 'blog:020:phase' in content
    assert content['blog:020:phase'].__class__ is BlogPhase
    assert ('blog:020:phase', 'BlogPhase (blog:phase)') in content.as_choices()


def test_phase_content(dummy_phase):
    assert dummy_phase.identifier == 'dummy:999:phase'
    assert str(dummy_phase) == 'DummyPhase (dummy:phase)'
    assert dummy_phase.has_feature('comment', models.Post)
