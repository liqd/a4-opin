import pytest
from django.core.urlresolvers import reverse


@pytest.mark.django_db
def test_anonymous_cannot_view_dashboard_overview(client):
    url = reverse('dashboard-overview')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_anonymous_cannot_view_dashboard_profile(client):
    url = reverse('dashboard-profile')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_authenticated_user_can_view_dashboard(client, user):
    url = reverse('dashboard-overview')
    login_url = reverse('login')
    client.post(login_url, {'email': user.email, 'password': 'password'})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_authenticated_user_can_view_profile(client, user):
    url = reverse('dashboard-profile')
    login_url = reverse('login')
    client.post(login_url, {'email': user.email, 'password': 'password'})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_authenticated_user_can_upload_avatar(client, user):
    url = reverse('dashboard-profile')
    login_url = reverse('login')
    client.post(login_url, {'email': user.email, 'password': 'password'})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_initiator_list_projects(client, project):
    user = project.organisation.initiators.first()
    client.login(username=user.email, password='password')
    url = reverse('dashboard-project-list')
    response = client.get(url)
    assert response.status_code == 200
    assert project in list(response.context_data['project_list']) == [project]


@pytest.mark.django_db
def test_initiator_edit_project(client, project):
    user = project.organisation.initiators.first()
    client.login(username=user.email, password='password')
    url = reverse('dashboard-project-edit', kwargs={'slug': project.slug})
    response = client.get(url)
    assert response.context_data['form'].instance == project
    assert response.status_code == 200
