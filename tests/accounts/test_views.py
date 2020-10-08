import datetime

import pytest
from django.contrib import auth
from django.urls import reverse

from tests.helpers import redirect_target

User = auth.get_user_model()


@pytest.mark.django_db
def test_anonymous_cannot_view_account_profile(client):
    url = reverse('account-profile')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_authenticated_user_can_view_profile(client, user, login_url):
    url = reverse('account-profile')
    client.post(login_url, {'email': user.email, 'password': 'password'})
    response = client.get(url)
    assert redirect_target(response) == 'account_login'


@pytest.mark.django_db
def test_authenticated_user_can_update_profile(client, user, login_url,
                                               smallImage):
    url = reverse('account-profile')
    client.login(username=user.email, password='password')
    response = client.get(url)
    assert response.status_code == 200

    birthday = datetime.date(2020, 1, 1)
    data = {'username': user.username,
            '_avatar': smallImage,
            'description': 'This is me.',
            'birthdate': birthday,
            'country': '',
            'city': '',
            'timezone': '',
            'gender': '',
            'languages': '',
            'twitter_handle': '',
            'facebook_handle': '',
            'instagram_handle': '',
            'get_notifications': ''
            }
    response = client.post(url, data)
    assert response.status_code == 302
    redirect = redirect_target(response)
    assert redirect == 'account-profile'

    response_get = client.get(reverse(redirect))
    assert response_get.status_code == 200
    assert response_get.context['user'].description == 'This is me.'
    assert response_get.context['user'].birthdate == birthday

    invalid_birthday = datetime.date(3000, 1, 1)
    data['birthday'] = invalid_birthday

    response = client.post(url, data)
    assert response.status_code == 302
    redirect = redirect_target(response)
    assert redirect == 'account-profile'

    response_get = client.get(reverse(redirect))
    assert response_get.status_code == 200
    assert response_get.context['user'].birthdate == birthday
