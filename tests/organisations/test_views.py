import pytest

from django.core.urlresolvers import reverse


@pytest.mark.django_db
def test_detail_view(client, organisation):
    url = reverse('organisation-detail', kwargs={'slug': organisation.slug})
    response = client.get(url)
    assert response.status_code == 200
