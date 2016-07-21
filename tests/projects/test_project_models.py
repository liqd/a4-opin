import os

import pytest
from django.conf import settings
from django.core.urlresolvers import reverse
from tests import helpers

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
@pytest.mark.parametrize('project__is_public', [False])
def test_is_privat(project):
    assert not project.is_public
    assert project.is_private


@pytest.mark.django_db
def test_image_validation_image_too_small(project_factory, smallImage):
    project = project_factory(image=smallImage)
    with pytest.raises(Exception) as e:
        project.full_clean()
    assert 'Image must be at least 600 pixels high' in str(e)


@pytest.mark.django_db
def test_image_big_enough(project_factory, bigImage):
    project = project_factory(image=bigImage)
    assert project.full_clean() is None


@pytest.mark.django_db
def test_delete_project(project_factory, ImagePNG):
    project = project_factory(image=ImagePNG)
    image_path = os.path.join(settings.MEDIA_ROOT, project.image.path)
    thumbnail_path = helpers.createThumbnail(project.image)
    assert os.path.isfile(thumbnail_path)
    assert os.path.isfile(image_path)
    count = models.Project.objects.all().count()
    assert count == 1
    project.delete()
    assert not os.path.isfile(thumbnail_path)
    assert not os.path.isfile(image_path)
    count = models.Project.objects.all().count()
    assert count == 0
