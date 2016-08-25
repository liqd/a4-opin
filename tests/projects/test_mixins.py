import pytest
from django.views.generic import ListView
from tests.apps.blog import models

from euth.projects import mixins


class DummyView(mixins.ProjectMixin, ListView):
    model = models.Post


@pytest.mark.django_db
def test_project_added(rf, phase):
    view = DummyView.as_view()
    project = phase.module.project
    request = rf.get('/project_name/ideas')
    response = view(request, project=project.slug)
    view_data = response.context_data['view']
    assert view_data.project == project
    assert view_data.phase == project.active_phase
    assert view_data.comment_enabled
    assert not view_data.rate_enabled
    assert not view_data.crud_enabled
