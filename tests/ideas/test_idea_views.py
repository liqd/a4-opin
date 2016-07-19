import pytest

from django.core.urlresolvers import reverse

from euth.ideas.models import Idea


@pytest.mark.django_db
def test_detail_view(client, idea):
    url = reverse('idea-detail', kwargs={'slug': idea.slug})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_view(client, module, user):
    count = Idea.objects.all().count()
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
    count = Idea.objects.all().count()
    assert count == 1


@pytest.mark.django_db
def test_update_view(client, idea, user):
    url = reverse('idea-update', kwargs={'slug': idea.slug})
    response = client.get(url)
    assert response.status_code == 403
    login_url = reverse('login')
    client.post(login_url, {'email': user.email, 'password': 'password'})
    response = client.get(url)
    assert response.status_code == 200
    data = {'description': 'description', 'name': idea.name}
    response = client.post(url, data)
    id = idea.pk
    updated_idea = Idea.objects.get(id=id)
    assert updated_idea.description == 'description'
    assert response.status_code == 302
