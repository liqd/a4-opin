import pytest
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError

from euth.comments import models as comments_models
from euth.documents.models import Document


@pytest.mark.django_db
def test_paragraph_save(paragraph):
    assert '<script>' not in paragraph.text


@pytest.mark.django_db
def test_document_clean(module, document_factory, user):

    document_factory(module=module)

    document2 = Document()
    document2.module = module
    document2.creator = user

    with pytest.raises(Exception) as e:
        document2.clean()

    assert e.type == ValidationError


@pytest.mark.django_db
def test_document_paragraphs_sorted(document, paragraph_factory):
    paragraph_factory(document=document, weight=2)
    paragraph2 = paragraph_factory(document=document, weight=1)

    assert document.paragraphs_sorted.first() == paragraph2


@pytest.mark.django_db
def test_paragraphs_comments(paragraph, comment_factory):
    contenttype = ContentType.objects.get_for_model(paragraph)

    for i in range(5):
        comment_factory(object_pk=paragraph.id, content_type=contenttype)
    comment_count = comments_models.Comment.objects.all().count()
    assert comment_count == paragraph.comments.count()
