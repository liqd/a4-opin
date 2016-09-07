import pytest
from django.core.urlresolvers import reverse

from tests.helpers import redirect_target


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


@pytest.mark.django_db
def test_dashboard_project_users(client, project, request_factory):
    url = reverse('dashboard-project-users', kwargs={'slug': project.slug})
    request0 = request_factory(project=project)
    request1 = request_factory(project=project)
    request2 = request_factory(project=project)

    response = client.get(url)
    assert redirect_target(response) == 'login'

    moderator = project.moderators.first()
    client.login(username=moderator.email, password='password')
    response = client.get(url)
    assert response.status_code == 200
    formset = response.context['formset']
    assert len(formset.forms) == 3
    assert formset.forms[0].instance == request0
    assert formset.forms[1].instance == request1
    assert formset.forms[2].instance == request2
    assert formset.extra == 0

    response = client.post(url, {
        'form-0-id': request0.pk,
        'form-0-action': 'accept',
        'form-1-id': request1.pk,
        'form-1-action': 'decline',
        'form-2-id': request2.pk,
        'form-2-action': '',
        'form-TOTAL_FORMS': '3',
        'form-INITIAL_FORMS': '3',
        'form-MAX_NUM_FORMS': '',
    })
    assert redirect_target(response) == 'dashboard-project-users'
    assert len(project.request_set.all()) == 1
    assert project.request_set.first() == request2
