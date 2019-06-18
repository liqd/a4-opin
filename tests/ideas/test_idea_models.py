import os

import pytest
from django.conf import settings
from django.urls import reverse

from adhocracy4.comments import models as comments_models
from adhocracy4.ratings import models as rating_models
from euth.ideas import models as idea_models
from tests import helpers


@pytest.mark.django_db
def test_absolute_url(idea):
    url = reverse('idea-detail', kwargs={'slug': idea.slug})
    assert idea.get_absolute_url() == url


@pytest.mark.django_db
def test_save(idea):
    assert '<script>' not in idea.description


@pytest.mark.django_db
def test_clean(idea):
    idea.clean()


@pytest.mark.django_db
def test_str(idea):
    idea_string = idea.__str__()
    assert idea_string == idea.name


@pytest.mark.django_db
def test_project(idea):
    assert idea.module.project == idea.project


@pytest.mark.django_db
def test_delete_idea(idea_factory, comment_factory, rating_factory, ImagePNG):
    idea = idea_factory(image=ImagePNG)
    image_path = os.path.join(settings.MEDIA_ROOT, idea.image.path)
    thumbnail_path = helpers.createThumbnail(idea.image)

    for i in range(5):
        comment_factory(content_object=idea)
    comment_count = comments_models.Comment.objects.all().count()
    assert comment_count == len(idea.comments.all())

    rating_factory(content_object=idea)
    rating_count = rating_models.Rating.objects.all().count()

    assert os.path.isfile(image_path)
    assert os.path.isfile(thumbnail_path)
    count = idea_models.Idea.objects.all().count()
    assert count == 1
    assert comment_count == 5
    assert rating_count == 1

    idea.delete()
    assert not os.path.isfile(image_path)
    assert not os.path.isfile(thumbnail_path)
    count = idea_models.Idea.objects.all().count()
    comment_count = comments_models.Comment.objects.all().count()
    rating_count = rating_models.Rating.objects.all().count()
    assert count == 0
    assert comment_count == 0
    assert rating_count == 0


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


@pytest.mark.django_db
def test_annotate_ratings(project, idea_factory, rating_factory):
    ideas = [idea_factory(name='idea{}'.format(i)) for i in range(3)]
    rating_factory(content_object=ideas[1], value=1)
    rating_factory(content_object=ideas[1], value=1)
    rating_factory(content_object=ideas[2], value=1)
    rating_factory(content_object=ideas[2], value=-1)
    rating_factory(content_object=ideas[2], value=-1)

    qs = idea_models.Idea.objects.annotate_positive_rating_count()
    assert qs.get(pk=ideas[0].pk).positive_rating_count == 0
    assert qs.get(pk=ideas[1].pk).positive_rating_count == 2
    assert qs.get(pk=ideas[2].pk).positive_rating_count == 1
    qs = idea_models.Idea.objects.annotate_negative_rating_count()
    assert qs.get(pk=ideas[0].pk).negative_rating_count == 0
    assert qs.get(pk=ideas[1].pk).negative_rating_count == 0
    assert qs.get(pk=ideas[2].pk).negative_rating_count == 2


@pytest.mark.django_db
def test_annotate_comment(project, idea_factory, comment_factory):
    ideas = [idea_factory(name='idea{}'.format(i)) for i in range(3)]
    comment_factory(content_object=ideas[2])
    comment_factory(content_object=ideas[1])
    comment_factory(content_object=ideas[1])

    qs = idea_models.Idea.objects.annotate_comment_count()
    assert qs.get(pk=ideas[0].pk).comment_count == 0
    assert qs.get(pk=ideas[1].pk).comment_count == 2
    assert qs.get(pk=ideas[2].pk).comment_count == 1


@pytest.mark.django_db
def test_combined_annotations(idea, comment_factory, rating_factory):
    qs = idea_models.Idea.objects.annotate_comment_count()\
                                 .annotate_positive_rating_count()
    assert qs.first().comment_count == 0
    assert qs.first().positive_rating_count == 0

    comment_factory(content_object=idea)
    rating_factory(content_object=idea, value=1)
    rating_factory(content_object=idea, value=1)

    qs = idea_models.Idea.objects.annotate_comment_count()\
                                 .annotate_positive_rating_count()
    assert qs.first().comment_count == 1
    assert qs.first().positive_rating_count == 2

    comment_factory(content_object=idea)
    comment_factory(content_object=idea)

    qs = idea_models.Idea.objects.annotate_comment_count()\
                                 .annotate_positive_rating_count()
    assert qs.first().comment_count == 3
    assert qs.first().positive_rating_count == 2
