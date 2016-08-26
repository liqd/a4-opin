import pytest
from dateutil.parser import parse
from freezegun import freeze_time
from tests.apps.blog import models as blog_models
from tests.apps.blog import views as blog_views

from euth.phases import models


@pytest.mark.django_db
def test_manager_active_phases(phase_factory):

    old_phase1 = phase_factory(
        start_date=parse('2013-01-01 17:00:00 UTC'),
        end_date=parse('2013-01-01 18:00:00 UTC')
    )
    module = old_phase1.module
    active_phase1 = phase_factory(
        module=module,
        start_date=parse('2013-01-01 18:00:00 UTC'),
        end_date=parse('2013-01-01 18:00:01 UTC')
    )
    active_phase2 = phase_factory(
        start_date=parse('2013-01-01 17:00:00 UTC'),
        end_date=parse('2013-01-01 19:00:00 UTC')
    )
    future_phase1 = phase_factory(
        start_date=parse('2013-01-01 18:00:01 UTC'),
        end_date=parse('2013-01-01 18:00:00 UTC')
    )

    with freeze_time('2013-01-01 18:00:00 UTC'):
        all_active_phases = models.Phase.objects.active_phases()
        assert active_phase1 in all_active_phases
        assert active_phase2 in all_active_phases
        assert old_phase1 not in all_active_phases
        assert future_phase1 not in all_active_phases

        module_active_phases = module.phase_set.active_phases()
        assert len(module_active_phases) == 1
        assert active_phase1 in module_active_phases


@pytest.mark.django_db
def test_blogapp_phase_view(phase):
    assert phase.view == blog_views.PostList


@pytest.mark.django_db
def test_blogapp_phase_feature(phase):
    assert phase.has_feature('comment', blog_models.Post)
