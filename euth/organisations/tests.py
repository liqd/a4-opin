import pytest
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.test import TestCase

from . import models


@pytest.fixture
def moderator():
    moderator = auth.get_user_model().objects.create_user(
        username='moderator',
        password='password',
        email='moderator@localhost')
    return moderator


@pytest.fixture
def org(moderator):
    organisation = models.Organisation.objects.create(
        name='test',
        slug='test',
        description_why='Thats why!',
        description_how='Thats how!',
        description='This is test!')
    organisation.initiators.add(moderator)
    return organisation


@pytest.mark.django_db
def test_detail_view(client, org):
    url = reverse('organisation-detail', kwargs={ 'slug': org.slug })
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_absolute_url(org):
    url = reverse('organisation-detail', kwargs={ 'slug': org.slug })
    assert org.get_absolute_url() == url
