import pytest
from dateutil.parser import parse
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import ListView
from freezegun import freeze_time

from adhocracy4.projects import models
from euth.projects import mixins
from tests.apps.fakeprojects.views import FakePhase0View, FakePhase1View


@pytest.fixture
def project_detail_view():
    class FakeProjectDetailView(mixins.PhaseDispatchMixin, ListView):
        model = models.Project

        def get(self, request, *args, **kwargs):
            return HttpResponse('project_detail')
    return FakeProjectDetailView.as_view()


@pytest.mark.django_db
def test_phase_dispatch_mixin(
    rf,
    project_detail_view,
    module,
    phase_factory
):
    project = module.project
    project_url = reverse('project-detail', args=[project.slug])

    phase1 = phase_factory(
        module=module,
        type='fakeprojects:010:phase',
        start_date=parse('2013-03-01 18:00:00 UTC'),
        end_date=parse('2013-03-02 18:00:00 UTC'),
        weight=0
    )
    phase_factory(
        module=module,
        type='fakeprojects:020:phase',
        start_date=parse('2013-03-03 18:00:00 UTC'),
        end_date=parse('2013-03-05 18:00:00 UTC'),
        weight=1
    )

    # Without any further specification via '?phase=' the last active
    # phase has to be returned.
    request = rf.get(project_url)
    response = project_detail_view(request, slug=project.slug)
    assert FakePhase1View.template_name in response.template_name
    assert FakePhase0View.template_name not in response.template_name

    # Requesting invalid phase parameter should return the last past
    # phase.
    request = rf.get("{0}?phase={1}".format(project_url, "A"*100))
    response = project_detail_view(request, slug=project.slug)
    assert FakePhase1View.template_name in response.template_name
    assert FakePhase0View.template_name not in response.template_name

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

    with freeze_time(phase1.end_date):
        # Requesting garbage should return the currently active phase.
        request = rf.get("{0}?phase={1}".format(project_url, "A"*100))
        response = project_detail_view(request, slug=project.slug)
        assert FakePhase0View.template_name in response.template_name
        assert FakePhase1View.template_name not in response.template_name

        # Without any further specification via '?phase=' return the
        # active phase.
        request = rf.get(project_url)
        response = project_detail_view(request, slug=project.slug)
        assert FakePhase0View.template_name in response.template_name
        assert FakePhase1View.template_name not in response.template_name
