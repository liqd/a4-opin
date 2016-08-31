import pytest
from django.http import HttpResponse
from django.views.generic import ListView, View
from freezegun import freeze_time
from tests.apps.blog import models as blog_models

from euth.projects import mixins, models


@pytest.fixture
def view_with_phase_dispatch():
    class FakeProjectDetailView(mixins.PhaseDispatchMixin, View):
        model = models.Project

        def get(self, request, *args, **kwargs):
            return HttpResponse('project_detail')
    return FakeProjectDetailView.as_view()


@pytest.mark.django_db
def test_phase_dispatch_mixin_phase(rf, view_with_phase_dispatch,
                                    active_project, active_phase):
    with freeze_time(active_phase.start_date):
        request = rf.get('/url')
        response = view_with_phase_dispatch(request, slug=active_project.slug)
        assert 'blog/post_list.html' in response.template_name


@pytest.mark.django_db
def test_phase_dispatch_mixin_default(rf, view_with_phase_dispatch,
                                      project):
    request = rf.get('/url')
    response = view_with_phase_dispatch(request, slug=project.slug)
    assert response.content == b'project_detail'


@pytest.mark.django_db
def test_project_mixin(rf, active_project, active_phase):
    class DummyView(mixins.ProjectMixin, ListView):
        model = blog_models.Post

    view = DummyView.as_view()
    request = rf.get('/project_name/ideas')

    with freeze_time(active_phase.start_date):
        response = view(request, project=active_project)

    response = view(request, project=active_project)
    view_data = response.context_data['view']
    assert view_data.project == active_project
    assert view_data.phase == active_phase
    assert view_data.comment_enabled
    assert not view_data.rate_enabled
    assert not view_data.crud_enabled
