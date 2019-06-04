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
