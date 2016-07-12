import pytest

from django.core import mail
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.models import AnonymousUser, Permission

from euth.user_management import forms
from euth.user_management import models

User = auth.get_user_model()

@pytest.mark.django_db
def test_login(client, user):
    login_url = reverse('login')
    response = client.get(login_url)
    assert response.status_code == 200

    response = client.post(
        login_url, {'email': user.email, 'password': 'password'})
    assert response.status_code == 302
    assert int(client.session['_auth_user_id']) == user.pk


@pytest.mark.django_db
def test_login_wrong_password(client, user):
    login_url = reverse('login')
    response = client.post(
        login_url, {'email': user.email, 'password': 'wrong_password'})
    assert response.status_code == 400


@pytest.mark.django_db
def test_login_no_password(client, user):
    login_url = reverse('login')
    response = client.post(
        login_url, {'email': user.email})
    assert response.status_code == 400


@pytest.mark.django_db
def test_form_valid_login(rf, user):
    request = rf.post('', {'email': user.email, 'password': 'password'})
    form = forms.LoginForm(request.POST)
    assert form.is_valid() == True
    testuser = form.login(request)
    assert user == testuser


@pytest.mark.django_db
def test_form_invalid_login(rf, user):
    request = rf.post(
        '', {'username': user.username, 'password': 'wrong_password'})
    form = forms.LoginForm(request.POST)
    assert form.is_valid() == False
    assert form.errors['__all__'] == ['password mismatch']


@pytest.mark.django_db
def test_logout(user, client):
    logged_in = client.login(email=user.email, password='password')
    assert logged_in == True
    logout_url = reverse('logout')
    response = client.get(logout_url)
    assert response.status_code == 200
    assert '_auth_user_id' not in client.session


@pytest.mark.django_db
def test_logout_with_next(user, client):
    logged_in = client.login(email=user.email, password='password')
    assert logged_in == True
    logout_url = reverse('logout')
    response = client.get(logout_url + '?next=/de/next_location')
    assert response.status_code == 302
    assert '/de/next_location' in response.url
    assert '_auth_user_id' not in client.session


@pytest.mark.django_db
def test_register(client):
    assert models.Registration.objects.all().count() == 0
    register_url = reverse('register')
    response = client.post(
        register_url, {
            'username': 'testuser2',
            'email': 'testuser@liqd.de',
            'password': 'password',
            'password_repeat': 'password'
        }
    )
    assert response.status_code == 302
    registration = models.Registration.objects.get(username='testuser2')
    activation_url = reverse('activate', kwargs={'token': registration.token})
    assert registration
    assert registration.email == 'testuser@liqd.de'
    assert len(mail.outbox) == 1
    assert 'You requested to register to' in mail.outbox[0].subject
    assert activation_url in mail.outbox[0].body

@pytest.mark.django_db
def test_reregister_same_username(client):
    data = {
        'username': 'testuser2',
        'email': 'testuser@liqd.de',
        'password': 'password',
        'password_repeat': 'password'
    }
    register_url = reverse('register')
    response = client.post(register_url, data)
    assert response.status_code == 302
    data['email'] = 'anotheremail@liqd.de'
    register_url = reverse('register')
    response = client.post(register_url, data)
    assert response.status_code == 400


@pytest.mark.django_db
def test_register_invalid(client):
    assert models.Registration.objects.all().count() == 0
    register_url = reverse('register')
    response = client.post(
        register_url + '?next=/', {
            'username': 'testuser2',
            'email': 'testuser@liqd.de',
            'password': 'password',
            'password_repeat': 'wrong_password'
        }
    )
    assert response.status_code == 400
    assert not models.Registration.objects.filter(username='testuser2')


@pytest.mark.django_db
def test_activate_user(registration, client):
    assert User.objects.all().count() == 0
    token = registration.token
    activate_url = reverse('activate', kwargs={'token': token})
    response = client.get(activate_url)
    assert response.status_code == 200

    response = client.post(activate_url, {'token': token})
    assert response.status_code == 302
    assert registration.next_action in response.url

    new_user = User.objects.get(email=registration.email)
    assert new_user
    assert new_user.username == registration.username


@pytest.mark.django_db
def test_reset(client, user):
    reset_req_url = reverse('reset_request')
    response = client.get(reset_req_url)
    assert response.status_code == 200

    response = client.post(reset_req_url, {
        'username_or_email': user.username,
        'next': '/de/my_nice_url'})
    assert response.status_code == 302
    reset = models.Reset.objects.get(user__username=user.username)
    assert reset

    reset_url = reverse('reset_password', kwargs={'token': reset.token })
    assert len(mail.outbox) == 1
    assert mail.outbox[0].to == [user.email]
    assert 'Reset password request for testserver' in mail.outbox[0].subject
    assert reset_url in mail.outbox[0].body

    response = client.get(reset_url)
    assert response.status_code == 200

    response = client.post(reset_url, {
        'password': 'password1',
        'password_repeat': 'password1',
        'token': reset.token })
    assert response.status_code == 302
    assert '/de/my_nice_url' in response.url
    assert user.password != User.objects.get(username=user.username).password


@pytest.mark.django_db
def test_request_reset_email(client, user):
    reset_req_url = reverse('reset_request')
    response = client.post(reset_req_url, { 'username_or_email': user.email })
    assert response.status_code == 302
    reset = models.Reset.objects.get(user__username=user.username)
    assert reset


@pytest.mark.django_db
def test_request_reset_error(client):
    reset_req_url = reverse('reset_request')
    response = client.post(reset_req_url)
    assert response.status_code == 400

    response = client.post(reset_req_url, { 'username_or_email': 'invalid_user' })
    assert response.status_code == 400


@pytest.mark.django_db
def test_reset_password_error(client, reset):
    reset_url = reverse('reset_password', kwargs={'token': reset.token })
    response = client.post(reset_url, {
        'password': 'password',
        'password_repeat': 'password_not_match',
        'token': reset.token })
    assert response.status_code == 400


@pytest.mark.django_db
def test_reset_password_invalid(client, reset):
    reset_url = reverse('reset_password', kwargs={'token': reset.token })
    response = client.post(reset_url, {
        'password': 'password',
        'password_repeat': 'password',
        'token': 'invalid_token' })
    assert response.status_code == 400
