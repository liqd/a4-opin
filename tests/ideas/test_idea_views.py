import pytest
from django.core.urlresolvers import reverse
from tests.utils import add_phase_to_project

from euth.ideas import models, phases


@pytest.mark.django_db
def test_detail_view(client, idea):
    url = reverse('idea-detail', kwargs={'slug': idea.slug})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_view(client, module, user):
    add_phase_to_project(module.project, phases.CollectPhase().identifier)
    count = models.Idea.objects.all().count()
    assert count == 0
    url = reverse('idea-create', kwargs={'slug': module.slug})
    response = client.get(url)
    assert response.status_code == 302
    login_url = reverse('login')
    client.post(login_url, {'email': user.email, 'password': 'password'})
    response = client.get(url)
    assert response.status_code == 200
    idea = {'name': 'Idea', 'description': 'description'}
    client.post(url, idea)
    assert response.status_code == 200
    count = models.Idea.objects.all().count()
    assert count == 1


@pytest.mark.django_db
def test_create_view_wrong_phase(client, module, user):
    add_phase_to_project(module.project, phases.RatePhase().identifier)
    url = reverse('idea-create', kwargs={'slug': module.slug})
    response = client.get(url)
    assert response.status_code == 302
    client.login(username=user.email, password='password')
    response = client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_update_view(client, idea, user):
    add_phase_to_project(idea.project, phases.CollectPhase().identifier)
    url = reverse('idea-update', kwargs={'slug': idea.slug})
    response = client.get(url)
    assert response.status_code == 302
    login_url = reverse('login')
    client.post(login_url, {'email': user.email, 'password': 'password'})
    response = client.get(url)
    assert response.status_code == 200
    data = {'description': 'description', 'name': idea.name}
    response = client.post(url, data)
    id = idea.pk
    updated_idea = models.Idea.objects.get(id=id)
    assert updated_idea.description == 'description'
    assert response.status_code == 302


@pytest.mark.django_db
def test_delete_view(client, idea, user):
    client.login(username=user.email, password='password')
    url = reverse('idea-delete', kwargs={'slug': idea.slug})
    response = client.post(url)
    assert response.status_code == 403

    add_phase_to_project(idea.project, phases.CollectPhase().identifier)
    response = client.post(url)
    assert response.status_code == 302
