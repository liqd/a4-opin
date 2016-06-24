import pytest
from datetime import timedelta

from django.http import HttpResponse
from django.utils import timezone
from django.contrib import auth
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from pytest_factoryboy import register

from ..organisations import models as org_models
from . import models
from . import factories

from ..organisations import factories as org_factories
register(org_factories.OrganisationFactory)
register(factories.ProjectFactory)


@pytest.mark.django_db
def test_get_absolute_url(project):
    project_url = reverse('project-detail', args=[project.slug])
    assert project.get_absolute_url() == project_url


@pytest.mark.django_db
def test_get_by_natural_key(project):
    assert project == models.Project.objects.get_by_natural_key(project.name)


@pytest.mark.django_db
def test_is_public(project):
    assert project.is_public
    assert not project.is_private

@pytest.mark.django_db
@pytest.mark.parametrize('project__visibility', [models.Visibility.private.value])
def test_is_privat(project):
    assert not project.is_public
    assert project.is_private


@pytest.mark.django_db
def test_list_view(client, project):
    url = reverse('project-list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_detail_view(client, project):
    project_url = reverse('project-detail', args=[project.slug])
    response = client.get(project_url)
    assert response.status_code == 200
