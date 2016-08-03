import pytest
from django.core.urlresolvers import reverse
from rest_framework import status


@pytest.mark.django_db
def test_anonymous_user_can_not_rate(apiclient):
    url = reverse('rates-list')
    data = {}
    response = apiclient.post(url, data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_authenticated_user_can_not_post_invalid_data(user, apiclient):
    apiclient.force_authenticate(user=user)
    url = reverse('rates-list')
    data = {}
    response = apiclient.post(url, data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_authenticated_user_can_post_valid_data(user, apiclient):
    apiclient.force_authenticate(user=user)
    url = reverse('rates-list')
    data = {
        'value': 1,
        'object_pk': 1,
        'content_type': 1
    }
    response = apiclient.post(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_authenticated_user_can_edit_own_rate(rate, apiclient):
    apiclient.force_authenticate(user=rate.user)
    data = {'value': 1}
    url = reverse('rates-detail', kwargs={'pk': rate.pk})
    response = apiclient.patch(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['value'] == 1


@pytest.mark.django_db
def test_authenticated_user_can_rate_higher_1(rate, apiclient):
    apiclient.force_authenticate(user=rate.user)
    data = {'value': 10}
    url = reverse('rates-detail', kwargs={'pk': rate.pk})
    response = apiclient.patch(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['value'] == 0


@pytest.mark.django_db
def test_authenticated_user_can_rate_lower_minus1(rate, apiclient):
    apiclient.force_authenticate(user=rate.user)
    data = {'value': -10}
    url = reverse('rates-detail', kwargs={'pk': rate.pk})
    response = apiclient.patch(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['value'] == 0


@pytest.mark.django_db
def test_anonymous_user_can_not_delete_rate(rate, apiclient):
    apiclient.force_authenticate(user=None)
    url = reverse('rates-detail', kwargs={'pk': rate.pk})
    response = apiclient.delete(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_authenticated_user_can_not_delete_rate(rate, user2, apiclient):
    url = reverse('rates-detail', kwargs={'pk': rate.pk})
    apiclient.force_authenticate(user=user2)
    response = apiclient.delete(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_creater_of_rate_can_set_zero(rate, apiclient):
    url = reverse('rates-detail', kwargs={'pk': rate.pk})
    apiclient.force_authenticate(user=rate.user)
    response = apiclient.delete(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['value'] == 0
