import os

import pytest
from django.conf import settings
from django.urls import reverse

from adhocracy4.comments import models as comments_models
from adhocracy4.ratings import models as rating_models
from euth.communitydebate import models as communitydebate_models
from tests import helpers


@pytest.mark.django_db
def test_file_upload_deleted_after_topic_deletion(topic_factory,
                                                  topic_file_upload_factory):
    topic = topic_factory()
    topic_file = topic_file_upload_factory(topic=topic)
    topic_file_path = os.path.join(settings.MEDIA_ROOT,
                                   topic_file.document.path)
    assert os.path.isfile(topic_file_path)

    topic.delete()
    assert not os.path.isfile(topic_file_path)


@pytest.mark.django_db
def test_file_upload_validation(topic_file_upload_factory, DocumentCSV):
    topic_file = topic_file_upload_factory(document=DocumentCSV)
    with pytest.raises(Exception) as e:
        topic_file.full_clean()
    assert 'Unsupported file format.' in str(e.value)
    topic_file.delete()


@pytest.mark.django_db
def test_absolute_url(topic):
    url = reverse('topic-detail', kwargs={'slug': topic.slug})
    assert topic.get_absolute_url() == url


@pytest.mark.django_db
def test_save(topic):
    assert '<script>' not in topic.description


@pytest.mark.django_db
def test_clean(topic):
    topic.clean()


@pytest.mark.django_db
def test_str(topic):
    topic_string = topic.__str__()
    assert topic_string == topic.name


@pytest.mark.django_db
def test_project(topic):
    assert topic.module.project == topic.project


@pytest.mark.django_db
def test_delete_topic(topic_factory, comment_factory, rating_factory,
                      ImagePNG):
    topic = topic_factory(image=ImagePNG)
    image_path = os.path.join(settings.MEDIA_ROOT, topic.image.path)
    thumbnail_path = helpers.createThumbnail(topic.image)

    for i in range(5):
        comment_factory(content_object=topic)
    comment_count = comments_models.Comment.objects.all().count()
    assert comment_count == len(topic.comments.all())

    rating_factory(content_object=topic)
    rating_count = rating_models.Rating.objects.all().count()

    assert os.path.isfile(image_path)
    assert os.path.isfile(thumbnail_path)
    count = communitydebate_models.Topic.objects.all().count()
    assert count == 1
    assert comment_count == 5
    assert rating_count == 1

    topic.delete()
    assert not os.path.isfile(image_path)
    assert not os.path.isfile(thumbnail_path)
    count = communitydebate_models.Topic.objects.all().count()
    comment_count = comments_models.Comment.objects.all().count()
    rating_count = rating_models.Rating.objects.all().count()
    assert count == 0
    assert comment_count == 0
    assert rating_count == 0


@pytest.mark.django_db
def test_image_deleted_after_update(topic_factory, ImagePNG):
    topic = topic_factory(image=ImagePNG)
    image_path = os.path.join(settings.MEDIA_ROOT, topic.image.path)
    thumbnail_path = helpers.createThumbnail(topic.image)

    assert os.path.isfile(image_path)
    assert os.path.isfile(thumbnail_path)

    topic.image = None
    topic.save()

    assert not os.path.isfile(image_path)
    assert not os.path.isfile(thumbnail_path)


@pytest.mark.django_db
def test_annotate_ratings(topic_factory, rating_factory):
    topics = [topic_factory(name='topic{}'.format(i)) for i in range(3)]
    rating_factory(content_object=topics[1], value=1)
    rating_factory(content_object=topics[1], value=1)
    rating_factory(content_object=topics[2], value=1)
    rating_factory(content_object=topics[2], value=-1)
    rating_factory(content_object=topics[2], value=-1)

    qs = communitydebate_models.Topic.objects.annotate_positive_rating_count()
    assert qs.get(pk=topics[0].pk).positive_rating_count == 0
    assert qs.get(pk=topics[1].pk).positive_rating_count == 2
    assert qs.get(pk=topics[2].pk).positive_rating_count == 1
    qs = communitydebate_models.Topic.objects.annotate_negative_rating_count()
    assert qs.get(pk=topics[0].pk).negative_rating_count == 0
    assert qs.get(pk=topics[1].pk).negative_rating_count == 0
    assert qs.get(pk=topics[2].pk).negative_rating_count == 2


@pytest.mark.django_db
def test_annotate_comment(topic_factory, comment_factory):
    topics = [topic_factory(name='topic{}'.format(i)) for i in range(3)]
    comment_factory(content_object=topics[2])
    comment_factory(content_object=topics[1])
    comment_factory(content_object=topics[1])

    qs = communitydebate_models.Topic.objects.annotate_comment_count()
    assert qs.get(pk=topics[0].pk).comment_count == 0
    assert qs.get(pk=topics[1].pk).comment_count == 2
    assert qs.get(pk=topics[2].pk).comment_count == 1


@pytest.mark.django_db
def test_combined_annotations(topic, comment_factory, rating_factory):
    qs = communitydebate_models.Topic.objects.annotate_comment_count().\
        annotate_positive_rating_count()
    assert qs.first().comment_count == 0
    assert qs.first().positive_rating_count == 0

    comment_factory(content_object=topic)
    rating_factory(content_object=topic, value=1)
    rating_factory(content_object=topic, value=1)

    qs = communitydebate_models.Topic.objects.annotate_comment_count().\
        annotate_positive_rating_count()
    assert qs.first().comment_count == 1
    assert qs.first().positive_rating_count == 2

    comment_factory(content_object=topic)
    comment_factory(content_object=topic)

    qs = communitydebate_models.Topic.objects.annotate_comment_count().\
        annotate_positive_rating_count()
    assert qs.first().comment_count == 3
    assert qs.first().positive_rating_count == 2
