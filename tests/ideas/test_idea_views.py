import pytest
from django.core.urlresolvers import reverse
from freezegun import freeze_time
from tests.helpers import redirect_target

from euth.ideas import models, phases


@pytest.mark.django_db
def test_detail_view(client, idea):
    url = reverse('idea-detail', kwargs={'slug': idea.slug})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize('active_phase__type',
                         [phases.CollectPhase().identifier])
def test_create_view(client, active_phase, user):
    module = active_phase.module
    with freeze_time(active_phase.start_date):
        count = models.Idea.objects.all().count()
        assert count == 0
        url = reverse('idea-create', kwargs={'slug': module.slug})
        response = client.get(url)
        assert response.status_code == 302
        assert redirect_target(response) == 'login'
        client.login(username=user.email, password='password')
        response = client.get(url)
        assert response.status_code == 200
        idea = {'name': 'Idea', 'description': 'description'}
        response = client.post(url, idea)
        assert response.status_code == 302
        assert redirect_target(response) == 'idea-detail'
        count = models.Idea.objects.all().count()
        assert count == 1


@pytest.mark.django_db
@pytest.mark.parametrize('active_phase__type',
                         [phases.RatePhase().identifier])
def test_create_view_wrong_phase(client, active_phase, user):
    module = active_phase.module
    with freeze_time(active_phase.start_date):
        url = reverse('idea-create', kwargs={'slug': module.slug})
        response = client.get(url)
        assert response.status_code == 302
        client.login(username=user.email, password='password')
        response = client.get(url)
        assert response.status_code == 403


@pytest.mark.django_db
@pytest.mark.parametrize('active_phase__type',
                         [phases.CollectPhase().identifier])
def test_update_view(client, active_phase, idea):
    idea.module = active_phase.module
    idea.save()
    user = idea.creator
    with freeze_time(active_phase.start_date):
        url = reverse('idea-update', kwargs={'slug': idea.slug})
        response = client.get(url)
        assert response.status_code == 302
        client.login(username=user.email, password='password')
        response = client.get(url)
        assert response.status_code == 200
        data = {'description': 'description', 'name': idea.name}
        response = client.post(url, data)
        id = idea.pk
        updated_idea = models.Idea.objects.get(id=id)
        assert updated_idea.description == 'description'
        assert response.status_code == 302


@pytest.mark.django_db
@pytest.mark.parametrize('active_phase__type',
                         [phases.CollectPhase().identifier])
def test_delete_view_wrong_user(client, active_phase, idea, user):
    idea.module = active_phase.module
    with freeze_time(active_phase.start_date):
        client.login(username=user.email, password='password')
        url = reverse('idea-delete', kwargs={'slug': idea.slug})
        response = client.post(url)
        assert response.status_code == 403
