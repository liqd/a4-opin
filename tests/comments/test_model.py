import pytest
from django.contrib.contenttypes.models import ContentType

from euth.comments import models as comments_models
from euth.ratings import models as rating_models


@pytest.mark.django_db
def test_delete_comment(comment_factory, rating_factory):
    comment = comment_factory()
    contenttype = ContentType.objects.get_for_model(comment)

    for i in range(5):
        comment_factory(object_pk=comment.id, content_type=contenttype)
    comment_count = comments_models.Comment.objects.all().count()

    rating_factory(object_pk=comment.id, content_type=contenttype)
    rating_count = rating_models.Rating.objects.all().count()

    assert comment_count == 6
    assert rating_count == 1

    comment.delete()

    comment_count = comments_models.Comment.objects.all().count()
    rating_count = rating_models.Rating.objects.all().count()
    assert comment_count == 0
    assert rating_count == 0
