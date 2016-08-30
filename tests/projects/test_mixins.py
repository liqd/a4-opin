import pytest
from django.views.generic import ListView
from freezegun import freeze_time
from tests.apps.blog import models

from euth.projects import mixins


class DummyView(mixins.ProjectMixin, ListView):
    model = models.Post


@pytest.mark.django_db
def test_project_added(rf, active_project, active_phase):
    view = DummyView.as_view()
    request = rf.get('/project_name/ideas')

    with freeze_time(active_phase.start_date):
        response = view(request, project=active_project.slug)

    view_data = response.context_data['view']
    assert view_data.project == active_project
    assert view_data.phase == active_phase
    assert view_data.comment_enabled
    assert not view_data.rate_enabled
    assert not view_data.crud_enabled
