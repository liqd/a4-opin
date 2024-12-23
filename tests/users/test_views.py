import re

import pytest
from allauth.account.models import EmailAddress
from django.contrib import auth
from django.core import mail
from django.urls import reverse

from euth.users import models

# from tests.helpers import redirect_target

User = auth.get_user_model()


@pytest.mark.django_db
def test_login(client, user, login_url):
    response = client.get(login_url)
    assert response.status_code == 200

    response = client.post(
        login_url, {'login': user.email, 'password': 'password'})
    assert response.status_code == 302
    assert int(client.session['_auth_user_id']) == user.pk


@pytest.mark.django_db
def test_login_wrong_password(client, user, login_url):
    response = client.post(
        login_url, {'login': user.email, 'password': 'wrong_password'})
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_no_password(client, user, login_url):
    response = client.post(
        login_url, {'login': user.email})
    assert response.status_code == 200


@pytest.mark.django_db
def test_logout(user, client, logout_url):
    logged_in = client.login(email=user.email, password='password')
    assert logged_in is True
    response = client.post(logout_url)
    assert response.status_code == 302
    assert '_auth_user_id' not in client.session


@pytest.mark.django_db
def test_logout_with_next(user, client, logout_url):
    logged_in = client.login(email=user.email, password='password')
    assert logged_in is True
    response = client.post(logout_url + '?next=/de/next_location')
    assert response.status_code == 302
    assert '/de/next_location' in response.url
    assert '_auth_user_id' not in client.session


# @pytest.mark.django_db
# def test_register(client, signup_url):
#     assert EmailAddress.objects.count() == 0
#     email = 'testuser@liqd.de'
#     response = client.post(
#         signup_url, {
#             'username': 'testuser',
#             'email': email,
#             'password1': 'password',
#             'password2': 'password',
#             'terms_of_use': 'on',
#             'captcha': 'testpass:0',
#         }
#     )
#     assert response.status_code == 302
#     assert EmailAddress.objects.filter(
#         email=email, verified=False
#     ).count() == 1
#     assert len(mail.outbox) == 1
#     confirmation_url = re.search(
#         r'(http://testserver/.*/)',
#         str(mail.outbox[0].body)
#     ).group(0)
#     confirm_email_response = client.get(confirmation_url)
#     assert confirm_email_response.status_code == 200
#     assert EmailAddress.objects.filter(
#         email=email, verified=False
#     ).count() == 1
#     confirm_email_response = client.post(confirmation_url)
#     assert confirm_email_response.status_code == 302
#     assert EmailAddress.objects.filter(
#         email=email, verified=True
#     ).count() == 1


# @pytest.mark.django_db
# def test_register_with_next(client, signup_url):
#     assert EmailAddress.objects.count() == 0
#     email = 'testuser2@liqd.de'
#     response = client.post(
#         signup_url, {
#             'username': 'testuser2',
#             'email': email,
#             'password1': 'password',
#             'password2': 'password',
#             'terms_of_use': 'on',
#             'next': '/en/projects/pppp/',
#             'captcha': 'testpass:0',
#         }
#     )
#     assert response.status_code == 302
#     assert EmailAddress.objects.filter(
#         email=email, verified=False
#     ).count() == 1
#     assert len(mail.outbox) == 1
#     confirmation_url = re.search(
#         r'(http://testserver/.*/?next=/en/projects/pppp/)',
#         str(mail.outbox[0].body)
#     ).group(0)
#     confirm_email_response = client.get(confirmation_url)
#     assert confirm_email_response.status_code == 200
#     assert EmailAddress.objects.filter(
#         email=email, verified=False
#     ).count() == 1
#     confirm_email_response = client.post(confirmation_url)
#     assert confirm_email_response.status_code == 302
#     assert redirect_target(confirm_email_response) == "project-detail"
#     assert EmailAddress.objects.filter(
#         email=email, verified=True
#     ).count() == 1


# @pytest.mark.django_db
# def test_reregister_same_username(client, signup_url):
#     assert EmailAddress.objects.count() == 0
#     data = {
#         'username': 'testuser3',
#         'email': 'testuser3@liqd.de',
#         'password1': 'password',
#         'password2': 'password',
#         'terms_of_use': 'on',
#         'captcha': 'testpass:0',
#     }
#     response = client.post(signup_url, data)
#     assert response.status_code == 302
#     assert EmailAddress.objects.count() == 1
#     data['email'] = 'anotheremail@liqd.de'
#     response = client.post(signup_url, data)
#     assert response.status_code == 302
#     assert EmailAddress.objects.count() == 1


@pytest.mark.django_db
def test_register_invalid(client, signup_url):
    # check registration is disabled
    # uncomment wrong password if registration is enabled
    username = 'testuser4'
    response = client.post(
        signup_url + '?next=/', {
            'username': username,
            'email': 'testuser4@liqd.de',
            'password1': 'password',
            'password2': 'password',
            # 'password2': 'wrong_password',
            'terms_of_use': 'on'
        }
    )
    assert response.status_code == 200
    assert models.User.objects.filter(username=username).count() == 0
    assert EmailAddress.objects.count() == 0


@pytest.mark.django_db
def test_reset(client, user):
    reset_req_url = reverse('account_reset_password')
    response = client.get(reset_req_url)
    assert response.status_code == 200
    response = client.post(reset_req_url, {'email': user.email})
    assert response.status_code == 302
    assert len(mail.outbox) == 1
    assert mail.outbox[0].to == [user.email]
    reset_url = re.search(
        r'(http://testserver/.*/)', str(mail.outbox[0].body)
    ).group(0)
    response = client.get(reset_url)
    assert response.status_code == 302
    reset_form_url = response.url
    response = client.get(reset_form_url)
    assert response.status_code == 200
    response = client.post(reset_form_url, {
        'password1': 'password1',
        'password2': 'password1',
    })
    assert response.status_code == 302
    assert response.url == '/'
    assert user.password != User.objects.get(username=user.username).password


@pytest.mark.django_db
def test_request_reset_error(client):
    reset_req_url = reverse('account_reset_password')
    response = client.post(reset_req_url)
    assert response.status_code == 200
    assert len(mail.outbox) == 0
    response = client.post(reset_req_url, {'email': 'invalid_user'})
    assert response.status_code == 200
    assert len(mail.outbox) == 0


@pytest.mark.django_db
def test_reset_password_error(client):
    reset_url = reverse('account_reset_password')
    response = client.post(reset_url, {
        'password1': 'password',
        'password2': 'password_not_match',
    })
    assert response.status_code == 200
    assert len(mail.outbox) == 0
