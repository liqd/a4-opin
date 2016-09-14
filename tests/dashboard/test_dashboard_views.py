import pytest
from django.core import mail
from django.core.urlresolvers import reverse
from tests.helpers import redirect_target


@pytest.mark.django_db
def test_anonymous_cannot_view_dashboard_profile(client):
    url = reverse('dashboard-profile')
    response = client.get(url)
    assert response.status_code == 302


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
    url = reverse('dashboard-project-list', kwargs={
        'organisation_slug': project.organisation.slug,
    })
    response = client.get(url)
    assert response.status_code == 200
    assert project in list(response.context_data['project_list']) == [project]


@pytest.mark.django_db
def test_initiator_edit_project(client, project):
    user = project.organisation.initiators.first()
    client.login(username=user.email, password='password')
    url = reverse('dashboard-project-edit', kwargs={
        'organisation_slug': project.organisation.slug,
        'slug': project.slug,
    })
    response = client.get(url)
    assert response.context_data['form'].instance == project
    assert response.status_code == 200


@pytest.mark.django_db
def test_dashboard_project_users(client, project, request_factory):
    url = reverse('dashboard-project-users', kwargs={
        'organisation_slug': project.organisation.slug,
        'slug': project.slug,
    })
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


@pytest.mark.django_db
def test_dashboard_project_invite(client, project):
    url = reverse('dashboard-project-invite', kwargs={
        'organisation_slug': project.organisation.slug,
        'slug': project.slug,
    })

    response = client.get(url)
    assert redirect_target(response) == 'login'

    moderator = project.moderators.first()
    client.login(username=moderator.email, password='password')
    response = client.get(url)
    assert response.status_code == 200

    response = client.post(url, {
        'emails': 'Jimmy Hendrix <j@he.ix>, james.dean@gmail.com'
    })
    assert redirect_target(response) == 'dashboard-project-users'
    assert len(project.invite_set.all()) == 2
    assert project.invite_set.all()[0].email == 'j@he.ix'
    assert project.invite_set.all()[1].email == 'james.dean@gmail.com'
    assert len(mail.outbox) == 2

    response = client.post(url, {
        'emails': 'j@he.ix'
    })

    errors = response.context_data['form']['emails'].errors
    assert errors == ['j@he.ix already invited']


@pytest.mark.django_db
def test_dashboard_project_invalid(client, project):
    url = reverse('dashboard-project-invite', kwargs={
        'organisation_slug': project.organisation.slug,
        'slug': project.slug,
    })
    moderator = project.moderators.first()
    client.login(username=moderator.email, password='password')

    response = client.post(url, {
        'emails': 'test@test.de foo@bar.de'
    })
    errors = response.context_data['form']['emails'].errors
    assert errors == ['@bar.de invalid email address']

    response = client.post(url, {
        'emails': 'test@foo, @aded'
    })
    errors = response.context_data['form']['emails'].errors
    assert errors == ['test@foo, @aded invalid email address']
