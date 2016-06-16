import pytest
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AnonymousUser, User, Permission
from django.test import TestCase
from .forms import LoginForm


from .views import register_user
from .views import login_user

@pytest.fixture
def testuser(db):
    testuser = User.objects.create_user(
        username='testuser',
        password='password')
    return testuser


@pytest.mark.django_db
def test_get_login_view(rf):
    login_url = reverse('login')
    request = rf.get(login_url)
    request.user = AnonymousUser()
    response = login_user(request)
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_login_view(client, testuser):
    login_url = reverse('login')
    response = client.post(
        login_url, {'username': 'testuser', 'password': 'password'})
    assert response.status_code == 302
    assert int(client.session['_auth_user_id']) == testuser.pk


@pytest.mark.django_db
def test_form_valid_login(rf, testuser):
    request = rf.post('', {'username': 'testuser', 'password': 'password'})
    form = LoginForm(request.POST)
    assert form.is_valid() == True
    user = form.login(request)
    assert user == testuser


@pytest.mark.django_db
def test_form_invalid_login(rf, testuser):
    request = rf.post('', {'username': 'testuser', 'password': 'wrong_password'})
    form = LoginForm(request.POST)
    assert form.is_valid() == False
    assert (dict(form.errors))['__all__'] == ['password mismatch']

