import pytest
from django.core.urlresolvers import reverse

from euth.projects import models

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
