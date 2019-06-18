import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_detail_view(client, organisation):
    url = reverse('organisation-detail', kwargs={'slug': organisation.slug})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_list_view(client, organisation_factory):
    for i in range(20):
        organisation_factory()
    url = reverse('organisation-list')
    response = client.get(url)
    assert len(response.context_data['object_list']) == 12
    assert response.context['is_paginated']
    assert response.status_code == 200
