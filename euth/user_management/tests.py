import pytest
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AnonymousUser, User, Permission
from django.test import TestCase
from .forms import LoginForm

from .models import Registration


from .views import register_user
from .views import login_user
from .views import logout_user


@pytest.fixture
def testuser(db):
    testuser = User.objects.create_user(
        username='testuser',
        password='password')
    return testuser


@pytest.fixture
def testregistration(db):
    testregistration = Registration.objects.create(
        username='testuser2',
        email='testuser2@liqd.de',
        password='password',
        token='b628de97-2a3a-4699-b4a4-16e64e4590f5',
        next_action='/de/my_super_interesting_content')
    return testregistration


@pytest.mark.django_db
def test_login(client, testuser):
    login_url = reverse('login')
    response = client.get(login_url)
    assert response.status_code == 200

    response = client.post(
        login_url, {'username': 'testuser', 'password': 'password'})
    assert response.status_code == 302
    assert int(client.session['_auth_user_id']) == testuser.pk


def test_login_wrong_password(client, testuser):
    login_url = reverse('login')
    response = client.post(
        login_url, {'username': 'testuser', 'password': 'wrong_password'})
    assert response.status_code == 400


def test_login_no_password(client, testuser):
    login_url = reverse('login')
    response = client.post(
        login_url, {'username': 'testuser'})
    assert response.status_code == 400


def test_form_valid_login(rf, testuser):
    request = rf.post('', {'username': 'testuser', 'password': 'password'})
    form = LoginForm(request.POST)
    assert form.is_valid() == True
    user = form.login(request)
    assert user == testuser


def test_form_invalid_login(rf, testuser):
    request = rf.post(
        '', {'username': 'testuser', 'password': 'wrong_password'})
    form = LoginForm(request.POST)
    assert form.is_valid() == False
    assert form.errors['__all__'] == ['password mismatch']


def test_logout(testuser, client):
    logged_in = client.login(username='testuser', password='password')
    assert logged_in == True
    logout_url = reverse('logout')
    response = client.get(logout_url)
    assert response.status_code == 200
    assert '_auth_user_id' not in client.session


def test_logout_with_next(testuser, client):
    logged_in = client.login(username='testuser', password='password')
    assert logged_in == True
    logout_url = reverse('logout')
    response = client.get(logout_url + '?next=/de/next_location')
    assert response.status_code == 302
    assert response.url == '/de/next_location'
    assert '_auth_user_id' not in client.session


@pytest.mark.django_db
def test_register(client):
    assert Registration.objects.all().count() == 0
    register_url = reverse('register')
    response = client.post(
        register_url, {
                'username': 'testuser2',
                'email':'testuser@liqd.de',
                'password': 'password',
                'password_repeat': 'password'
            }
        )
    assert Registration.objects.all().count() == 1


@pytest.mark.django_db
def test_register_invalid(client):
    assert Registration.objects.all().count() == 0
    register_url = reverse('register')
    response = client.post(
        register_url + '?next=/', {
                'username': 'testuser2',
                'email':'testuser@liqd.de',
                'password': 'password',
                'password_repeat': 'wrong_password'
            }
        )
    assert Registration.objects.all().count() == 0

def test_activate_user(testregistration, client):
    assert User.objects.all().count() == 0
    token = testregistration.token
    activate_url = reverse('activate', kwargs={'token': token})
    client.post(activate_url, {})
    #assert User.objects.all().count() == 1










