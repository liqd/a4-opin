import pytest
from dateutil.parser import parse
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView
from freezegun import freeze_time

from adhocracy4.projects import models
from euth.projects import mixins
from tests.apps.fakeprojects.phases import FakePhase0
from tests.apps.fakeprojects.phases import FakePhase1
from tests.apps.fakeprojects.views import FakePhase0View
from tests.apps.fakeprojects.views import FakePhase1View


@pytest.fixture
def phase1(module, phase_factory):
    return phase_factory(
        module=module,
        type=FakePhase0().identifier,
        start_date=parse('2013-03-01 18:00:00 UTC'),
        end_date=parse('2013-03-02 18:00:00 UTC'),
        weight=0
    )


@pytest.fixture
def phase2(module, phase_factory):
    return phase_factory(
        module=module,
        type=FakePhase1().identifier,
        start_date=parse('2013-03-03 18:00:00 UTC'),
        end_date=parse('2013-03-05 18:00:00 UTC'),
        weight=1
    )


@pytest.fixture
def project_detail_view():
    class FakeProjectDetailView(mixins.PhaseDispatchMixin, ListView):
        model = models.Project
        project_url_kwarg = 'slug'

        def get(self, request, *args, **kwargs):
            return HttpResponse('project_detail')

    return FakeProjectDetailView.as_view()


@pytest.fixture
def dummy_view():
    class DummyView(mixins.ProjectPhaseMixin, ListView):
        model = models.Project

    return DummyView.as_view()


@pytest.mark.django_db
def test_phase_dispatch_mixin_return_super(
    rf,
    project_detail_view,
    module
):
    project = module.project
    project_url = reverse('project-detail', args=[project.slug])

    # Without any further specification via '?phase=' the last
    # phase has to be returned.
    request = rf.get(project_url)
    response = project_detail_view(request, slug=project.slug)
    assert response.content == b'project_detail'
    assert FakePhase0View.template_name not in \
        getattr(response, 'template_name', [])
    assert FakePhase1View.template_name not in \
        getattr(response, 'template_name', [])

    # Requesting invalid phase parameter should return the last past
    # phase.
    request = rf.get("{0}?phase={1}".format(project_url, "A" * 100))
    response = project_detail_view(request, slug=project.slug)
    assert response.content == b'project_detail'
    assert FakePhase0View.template_name not in \
        getattr(response, 'template_name', [])
    assert FakePhase1View.template_name not in \
        getattr(response, 'template_name', [])

    # If project has no phase, no phase can be returned. So this should
    # behave like passing nothing.
    request = rf.get("{0}?phase={1}".format(project_url, 0))
    response = project_detail_view(request, slug=project.slug)
    assert response.content == b'project_detail'
    assert FakePhase0View.template_name not in \
        getattr(response, 'template_name', [])
    assert FakePhase1View.template_name not in \
        getattr(response, 'template_name', [])


@pytest.mark.django_db
def test_phase_dispatch_mixin_return_last_phase(
    rf,
    project_detail_view,
    phase1,
    phase2
):
    project = phase1.module.project
    project_url = reverse('project-detail', args=[project.slug])

    # Without any further specification via '?phase=' the last
    # phase has to be returned.
    request = rf.get(project_url)
    response = project_detail_view(request, slug=project.slug)
    assert FakePhase1View.template_name in response.template_name
    assert FakePhase0View.template_name not in response.template_name

    # Requesting invalid phase parameter should return the last past
    # phase.
    request = rf.get("{0}?phase={1}".format(project_url, "A" * 100))
    response = project_detail_view(request, slug=project.slug)
    assert FakePhase1View.template_name in response.template_name
    assert FakePhase0View.template_name not in response.template_name


@pytest.mark.django_db
def test_phase_dispatch_mixin_return_selected_phase(
    rf,
    project_detail_view,
    phase1,
    phase2
):
    project = phase1.module.project
    project_url = reverse('project-detail', args=[project.slug])

    # Requesting the phase by passing their weight should return the
    # corresponding view. This is basically the normal usage.
    request = rf.get("{0}?phase={1}".format(project_url, 0))
    response = project_detail_view(request, slug=project.slug)
    assert FakePhase0View.template_name in response.template_name
    assert FakePhase1View.template_name not in response.template_name

    request = rf.get("{0}?phase={1}".format(project_url, 1))
    response = project_detail_view(request, slug=project.slug)
    assert FakePhase1View.template_name in response.template_name
    assert FakePhase0View.template_name not in response.template_name


@pytest.mark.django_db
def test_phase_dispatch_mixin_return_active_phase(
    rf,
    project_detail_view,
    phase1,
    phase2
):
    project = phase1.module.project
    project_url = reverse('project-detail', args=[project.slug])

    with freeze_time(phase1.start_date):
        # Requesting garbage should return the currently active phase.
        request = rf.get("{0}?phase={1}".format(project_url, "A" * 100))
        response = project_detail_view(request, slug=project.slug)
        assert FakePhase0View.template_name in response.template_name
        assert FakePhase1View.template_name not in response.template_name

        # Without any further specification via '?phase=' return the
        # active phase.
        request = rf.get(project_url)
        response = project_detail_view(request, slug=project.slug)
        assert FakePhase0View.template_name in response.template_name
        assert FakePhase1View.template_name not in response.template_name


@pytest.mark.django_db
def test_project_phase_mixin_return_last_phase(
    rf,
    dummy_view,
    phase1,
    phase2
):
    project = phase1.module.project
    project_url = reverse('project-detail', args=[project.slug])

    # Without any further specification via '?phase=' the last active
    # phase has to be returned.
    request = rf.get(project_url)
    response = dummy_view(request, slug=project.slug, project=project)
    view_data = response.context_data['view']
    assert view_data.project == project
    assert view_data.phase == phase2
    assert view_data.module == phase2.module

    # Requesting invalid phase parameter should return the last past
    # phase.
    request = rf.get("{0}?phase={1}".format(project_url, "A" * 100))
    response = dummy_view(request, slug=project.slug, project=project)
    view_data = response.context_data['view']
    assert view_data.project == project
    assert view_data.phase == phase2


@pytest.mark.django_db
def test_project_phase_mixin_return_select_phase(
    rf,
    dummy_view,
    phase1,
    phase2
):
    project = phase1.module.project
    project_url = reverse('project-detail', args=[project.slug])

    # Requesting the phase by passing their weight should return the
    # corresponding view. This is basically the normal usage.
    request = rf.get("{0}?phase={1}".format(project_url, 0))
    response = dummy_view(request, slug=project.slug, project=project)
    view_data = response.context_data['view']
    assert view_data.project == project
    assert view_data.phase == phase1

    request = rf.get("{0}?phase={1}".format(project_url, 1))
    response = dummy_view(request, slug=project.slug, project=project)
    view_data = response.context_data['view']
    assert view_data.project == project
    assert view_data.phase == phase2


@pytest.mark.django_db
def test_project_phase_mixin_return_active_phase(
    rf,
    dummy_view,
    phase1,
    phase2
):
    project = phase1.module.project
    project_url = reverse('project-detail', args=[project.slug])

    with freeze_time(phase2.start_date):
        # Requesting garbage should return the currently active phase.
        request = rf.get("{0}?phase={1}".format(project_url, "A" * 100))
        response = dummy_view(request, slug=project.slug, project=project)
        view_data = response.context_data['view']
        assert view_data.project == project
        assert view_data.phase == phase2

        # Without any further specification via '?phase=' return the
        # active phase.
        request = rf.get(project_url)
        response = dummy_view(request, slug=project.slug, project=project)
        view_data = response.context_data['view']
        assert view_data.project == project
        assert view_data.phase == phase2
