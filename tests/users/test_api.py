import pytest
from django.urls import reverse
from rest_framework import status

from tests.factories import UserFactory


@pytest.mark.django_db
def test_anonymous_user_cant_access_api(apiclient):
    url = reverse('users-list')
    response = apiclient.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_cant_access_user_list_without_param(apiclient, user):
    url = reverse('users-list')
    apiclient.force_authenticate(user=user)
    response = apiclient.get(url)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_cant_access_user_list_without_search_param(apiclient, user):
    url = reverse('users-list')
    url += '?sea'
    apiclient.force_authenticate(user=user)
    response = apiclient.get(url)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_cant_access_user_list_with_empty_search_param(apiclient, user):
    url = reverse('users-list')
    url += '?search='
    apiclient.force_authenticate(user=user)
    response = apiclient.get(url)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_can_access_user_list(apiclient):
    user1 = UserFactory(username='Cersei')
    user2 = UserFactory(username='Arya')
    url = reverse('users-list')
    url += '?search=A'
    apiclient.force_authenticate(user=user1)
    response = apiclient.get(url)
    assert response.status_code == status.HTTP_200_OK
    user_data = response.data[0]
    assert len(response.data) == 1
    assert user_data['id'] == user2.pk

    user3 = UserFactory(username='Aemon')
    response = apiclient.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    user_data0 = response.data[0]
    user_data1 = response.data[1]
    assert user_data0['id'] == user3.pk
    assert user_data1['id'] == user2.pk
