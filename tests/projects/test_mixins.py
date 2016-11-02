import pytest
from dateutil.parser import parse
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
def test_phase_dispatch_mixin_phase(rf, view_with_phase_dispatch, phase):
    project = phase.module.project
    with freeze_time(phase.start_date):
        request = rf.get('/url')
        response = view_with_phase_dispatch(request, slug=project.slug)
        assert 'blog/post_list.html' in response.template_name


@pytest.mark.django_db
def test_phase_dispatch_mixin_default(rf, view_with_phase_dispatch,
                                      project):
    request = rf.get('/url')
    response = view_with_phase_dispatch(request, slug=project.slug)
    assert response.content == b'project_detail'


@pytest.mark.django_db
def test_project_mixin(rf, phase):
    project = phase.module.project

    class DummyView(mixins.ProjectMixin, ListView):
        model = blog_models.Post

    view = DummyView.as_view()
    request = rf.get('/project_name/ideas')

    with freeze_time(phase.start_date):
        response = view(request, project=project)

    response = view(request, project=project)
    view_data = response.context_data['view']
    assert view_data.project == project
    assert view_data.phase == phase


@pytest.mark.django_db
def test_project_inject_phase_after_finish(rf, phase_factory):
    phase = phase_factory(
        start_date=parse('2013-01-01 17:00:00 UTC'),
        end_date=parse('2013-01-01 18:00:00 UTC')
    )
    module = phase.module
    project = module.project

    class DummyView(mixins.ProjectMixin, ListView):
        model = blog_models.Post

    view = DummyView.as_view()
    request = rf.get('/project_name/ideas')

    with freeze_time(phase.end_date):
        response = view(request, project=project)

    response = view(request, project=project)
    view_data = response.context_data['view']
    assert view_data.project == project
    assert view_data.phase == phase
