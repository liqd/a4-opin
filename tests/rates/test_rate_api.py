import pytest
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from rest_framework import status


@pytest.mark.django_db
def test_anonymous_user_can_not_get_rate_list(apiclient):
    url = reverse('rates-list')
    response = apiclient.get(url, format='json')
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_authenticated_user_can_not_get_rate_list(apiclient, user):
    url = reverse('rates-list')
    apiclient.force_authenticate(user=user)
    response = apiclient.get(url, format='json')
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


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
def test_authenticated_user_can_edit_own_rate(rate_factory,
                                              comment,
                                              apiclient):
    ct = ContentType.objects.get_for_model(comment)
    rate = rate_factory(object_pk=comment.id, content_type=ct)
    apiclient.force_authenticate(user=rate.user)
    data = {'value': 1}
    url = reverse('rates-detail', kwargs={'pk': rate.pk})
    response = apiclient.patch(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['value'] == 1


@pytest.mark.django_db
def test_authenticated_user_can_rate_higher_1(rate_factory,
                                              comment,
                                              apiclient):
    ct = ContentType.objects.get_for_model(comment)
    rate = rate_factory(object_pk=comment.id, content_type=ct)
    apiclient.force_authenticate(user=rate.user)
    data = {'value': 10}
    url = reverse('rates-detail', kwargs={'pk': rate.pk})
    response = apiclient.patch(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['value'] == 1


@pytest.mark.django_db
def test_authenticated_user_can_rate_lower_minus1(rate_factory,
                                                  comment,
                                                  apiclient):
    ct = ContentType.objects.get_for_model(comment)
    rate = rate_factory(object_pk=comment.id, content_type=ct)
    apiclient.force_authenticate(user=rate.user)
    data = {'value': -10}
    url = reverse('rates-detail', kwargs={'pk': rate.pk})
    response = apiclient.patch(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['value'] == -1


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
def test_creater_of_rate_can_set_zero(rate_factory, comment,  apiclient):
    ct = ContentType.objects.get_for_model(comment)
    rate = rate_factory(object_pk=comment.id, content_type=ct)
    url = reverse('rates-detail', kwargs={'pk': rate.pk})
    apiclient.force_authenticate(user=rate.user)
    response = apiclient.delete(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['value'] == 0


@pytest.mark.django_db
def test_meta_info_of_rate(rate_factory, comment,  apiclient, user, user2):
    ct = ContentType.objects.get_for_model(comment)
    pk = comment.pk
    url = reverse('rates-list')
    apiclient.force_authenticate(user)
    data = {
        'value': 1,
        'object_pk': pk,
        'content_type': ct.pk
    }
    response = apiclient.post(url, data, format='json')
    rate_id = response.data['id']
    assert response.status_code == status.HTTP_200_OK
    assert response.data['value'] == 1
    assert response.data['meta_info']['positive_rates_on_same_object'] == 1
    assert response.data['meta_info']['user_rate_on_same_object_value'] == 1
    assert response.data['meta_info']['user_rate_on_same_object_id'] == rate_id
    apiclient.force_authenticate(user2)
    response = apiclient.post(url, data, format='json')
    rate_id = response.data['id']
    assert response.status_code == status.HTTP_200_OK
    assert response.data['value'] == 1
    assert response.data['meta_info']['positive_rates_on_same_object'] == 2
    assert response.data['meta_info']['user_rate_on_same_object_value'] == 1
    assert response.data['meta_info']['user_rate_on_same_object_id'] == rate_id
