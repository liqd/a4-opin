import pytest
from tests.apps.blog import models as blog_models
from tests.apps.blog import views as blog_views

from euth.phases import models


@pytest.mark.django_db
def test_manager_all_phases(phase):
    all_phases = models.Phase.objects.all_phases(phase.module.project)
    assert list(all_phases) == [phase]


@pytest.mark.django_db
def test_manager_active_phase(phase_factory):
    phase1 = phase_factory()
    phase_factory(module=phase1.module)
    active = models.Phase.objects.active_phase(phase1.module.project)
    assert active == phase1


@pytest.mark.django_db
def test_blogapp_phase_view(phase):
    assert phase.view == blog_views.PostDetail


@pytest.mark.django_db
def test_blogapp_phase_feature(phase):
    assert phase.has_feature('comment', blog_models.Post)
