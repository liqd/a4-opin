import pytest
from django.contrib import auth
from django.core import mail
from django.core.urlresolvers import reverse
from tests.helpers import redirect_target

User = auth.get_user_model()


@pytest.mark.django_db
def test_anonymous_cannot_view_dashboard_profile(client):
    url = reverse('dashboard-profile')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_authenticated_user_can_view_profile(client, user, login_url):
    url = reverse('dashboard-profile')
    client.post(login_url, {'email': user.email, 'password': 'password'})
    response = client.get(url)
    assert redirect_target(response) == 'account_login'


@pytest.mark.django_db
def test_authenticated_user_can_upload_avatar(client, user, login_url):
    url = reverse('dashboard-profile')
    login_url = reverse('login')
    client.post(login_url, {'email': user.email, 'password': 'password'})
    response = client.get(url)
    assert redirect_target(response) == 'account_login'


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
def test_dashboard_project_users(client, project, user_factory,
                                 request_factory, invite_factory):
    url = reverse('dashboard-project-users', kwargs={
        'organisation_slug': project.organisation.slug,
        'slug': project.slug,
    })
    request0 = request_factory(project=project)
    request1 = request_factory(project=project)
    request2 = request_factory(project=project)
    invite0 = invite_factory(project=project)
    invite1 = invite_factory(project=project)
    user0 = user_factory(email='test@test1.de')
    user1 = user_factory(email='test@test2.de')
    project.participants.add(user0)
    project.participants.add(user1)

    response = client.get(url)
    assert redirect_target(response) == 'account_login'

    moderator = project.moderators.first()
    client.login(username=moderator.email, password='password')
    response = client.get(url)
    assert response.status_code == 200
    multiform = response.context['form']
    assert len(multiform['requests'].forms) == 3
    assert multiform['requests'].forms[0].instance == request0
    assert multiform['requests'].forms[1].instance == request1
    assert multiform['requests'].forms[2].instance == request2
    assert multiform['requests'].extra == 0
    assert len(multiform['invites'].forms) == 2
    assert multiform['invites'].forms[0].instance == invite0
    assert multiform['invites'].forms[1].instance == invite1
    assert len(multiform['users'].forms) == 2
    assert multiform['users'].forms[0].instance == user0
    assert multiform['users'].forms[1].instance == user1

    response = client.post(url, {
        'requests-0-id': request0.pk,
        'requests-0-action': 'accept',
        'requests-1-id': request1.pk,
        'requests-1-action': 'decline',
        'requests-2-id': request2.pk,
        'requests-2-action': '',
        'requests-TOTAL_FORMS': '3',
        'requests-INITIAL_FORMS': '3',
        'requests-MAX_NUM_FORMS': '',
        'invites-TOTAL_FORMS': '2',
        'invites-INITIAL_FORMS': '2',
        'invites-MAX_NUM_FORMS': '',
        'invites-0-id': invite0.pk,
        'invites-0-delete': 'on',
        'invites-1-id': invite1.pk,
        'users-TOTAL_FORMS': '2',
        'users-INITIAL_FORMS': '2',
        'users-MAX_NUM_FORMS': '',
        'users-0-id': user0.id,
        'users-0-delete': 'on',
        'users-1-id': user1.id,
        'users-1-delete': '',
    })
    assert redirect_target(response) == 'dashboard-project-users'
    assert len(project.request_set.all()) == 1
    assert project.request_set.first() == request2
    assert len(project.invite_set.all()) == 1
    assert project.invite_set.first() == invite1
    assert len(project.participants.all()) == 2
    assert not project.participants.filter(username=user0.username).exists()
    assert User.objects.filter(username=user0.username).exists()


@pytest.mark.django_db
def test_dashboard_project_invite(client, project):
    url = reverse('dashboard-project-invite', kwargs={
        'organisation_slug': project.organisation.slug,
        'slug': project.slug,
    })

    response = client.get(url)
    assert redirect_target(response) == 'account_login'

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
