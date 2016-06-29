import pytest

from django.core.urlresolvers import reverse

from euth.organisations import models


@pytest.mark.django_db
def test_absolute_url(organisation):
    url = reverse('organisation-detail', kwargs={'slug': organisation.slug})
    assert organisation.get_absolute_url() == url


@pytest.mark.django_db
def test_natural_keys(organisation):
    assert models.Organisation.objects.get_by_natural_key(
        organisation.name) == organisation
