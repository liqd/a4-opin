import os
import pytest

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from tests import helpers

from euth.comments import models as comments_models
from euth.ideas import models as idea_models


@pytest.mark.django_db
def test_absolute_url(idea):
    url = reverse('idea-detail', kwargs={'slug': idea.slug})
    assert idea.get_absolute_url() == url


@pytest.mark.django_db
def test_save(idea):
    assert '<script>' not in idea.description


@pytest.mark.django_db
def test_str(idea):
    idea_string = idea.__str__()
    assert idea_string == idea.name


@pytest.mark.django_db
def test_project(idea):
    assert idea.module.project == idea.project


@pytest.mark.django_db
def test_delete_idea(idea_factory, comment_factory, ImagePNG):
    idea = idea_factory(image=ImagePNG)
    image_path = os.path.join(settings.MEDIA_ROOT, idea.image.path)
    thumbnail_path = helpers.createThumbnail(idea.image)
    contenttype = ContentType.objects.get_for_model(idea)

    for i in range(5):
        comment_factory(object_pk=idea.id, content_type=contenttype)

    comment_count = comments_models.Comment.objects.all().count()

    assert os.path.isfile(image_path)
    assert os.path.isfile(thumbnail_path)
    count = idea_models.Idea.objects.all().count()
    assert count == 1
    assert comment_count == 5

    idea.delete()
    assert not os.path.isfile(image_path)
    assert not os.path.isfile(thumbnail_path)
    count = idea_models.Idea.objects.all().count()
    comment_count = comments_models.Comment.objects.all().count()
    assert count == 0
    assert comment_count == 0


@pytest.mark.django_db
def test_image_deleted_after_update(idea_factory, ImagePNG):
    idea = idea_factory(image=ImagePNG)
    image_path = os.path.join(settings.MEDIA_ROOT, idea.image.path)
    thumbnail_path = helpers.createThumbnail(idea.image)

    assert os.path.isfile(image_path)
    assert os.path.isfile(thumbnail_path)

    idea.image = None
    idea.save()

    assert not os.path.isfile(image_path)
    assert not os.path.isfile(thumbnail_path)
