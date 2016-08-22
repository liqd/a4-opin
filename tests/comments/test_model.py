import pytest
from django.contrib.contenttypes.models import ContentType

from euth.comments import models as comments_models
from euth.rates import models as rate_models


@pytest.mark.django_db
def test_delete_comment(comment_factory, rate_factory):
    comment = comment_factory()
    contenttype = ContentType.objects.get_for_model(comment)

    for i in range(5):
        comment_factory(object_pk=comment.id, content_type=contenttype)
    comment_count = comments_models.Comment.objects.all().count()

    rate_factory(object_pk=comment.id, content_type=contenttype)
    rate_count = rate_models.Rate.objects.all().count()

    assert comment_count == 6
    assert rate_count == 1

    comment.delete()

    comment_count = comments_models.Comment.objects.all().count()
    rate_count = rate_models.Rate.objects.all().count()
    assert comment_count == 0
    assert rate_count == 0
