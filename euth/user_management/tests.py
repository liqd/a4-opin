import pytest

from pytest_factoryboy import register

from django.core import mail
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AnonymousUser, User, Permission

from . import factories
from . import forms
from . import models

register(factories.UserFactory)
register(factories.RegistrationFactory)


@pytest.mark.django_db
def test_login(client, user):
    login_url = reverse('login')
    response = client.get(login_url)
    assert response.status_code == 200

    response = client.post(
        login_url, {'username': user.username, 'password': 'password'})
    assert response.status_code == 302
    assert int(client.session['_auth_user_id']) == user.pk


@pytest.mark.django_db
def test_login_wrong_password(client, user):
    login_url = reverse('login')
    response = client.post(
        login_url, {'username': user.username, 'password': 'wrong_password'})
    assert response.status_code == 400


@pytest.mark.django_db
def test_login_no_password(client, user):
    login_url = reverse('login')
    response = client.post(
        login_url, {'username': user.username})
    assert response.status_code == 400


@pytest.mark.django_db
def test_form_valid_login(rf, user):
    request = rf.post('', {'username': user.username, 'password': 'password'})
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
    logged_in = client.login(username=user.username, password='password')
    assert logged_in == True
    logout_url = reverse('logout')
    response = client.get(logout_url)
    assert response.status_code == 200
    assert '_auth_user_id' not in client.session


@pytest.mark.django_db
def test_logout_with_next(user, client):
    logged_in = client.login(username=user.username, password='password')
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
    assert response.status_code == 200
    registration = models.Registration.objects.get(username='testuser2')
    activation_url = reverse('activate', kwargs={'token': registration.token})
    assert registration
    assert registration.email == 'testuser@liqd.de'
    assert len(mail.outbox) == 1
    assert 'You created an account for' in mail.outbox[0].subject
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
    assert response.status_code == 200
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

    new_user = User.objects.get(username=registration.username)
    assert new_user
    #print(registration.email)
    assert new_user.email == registration.email
