import pytest
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError

from adhocracy4.comments import models as comments_models
from euth.documents.models import Document


@pytest.mark.django_db
def test_paragraph_save(paragraph):
    assert '<script>' not in paragraph.text


@pytest.mark.django_db
def test_document_clean(document):
    another_document = Document(
        module=document.module,
        creator=document.creator
    )

    with pytest.raises(ValidationError):
        another_document.clean()


@pytest.mark.django_db
def test_paragraph_knows_project_and_module(paragraph):
    assert paragraph.project == paragraph.document.project
    assert paragraph.module == paragraph.document.module


@pytest.mark.django_db
def test_document_paragraphs_sorted(document, paragraph_factory):
    paragraph_factory(document=document, weight=2)
    paragraph2 = paragraph_factory(document=document, weight=1)

    assert document.paragraphs.first() == paragraph2


@pytest.mark.django_db
def test_paragraphs_comments(paragraph, comment_factory):
    for i in range(5):
        comment_factory(content_object=paragraph)
    comment_count = comments_models.Comment.objects.all().count()
    assert comment_count == paragraph.comments.count()


@pytest.mark.django_db
def test_delete_document(document, comment_factory):
    for i in range(5):
        comment_factory(content_object=document)

    def comments_for_document(document):
        return comments_models.Comment.objects.filter(
            object_pk=document.pk,
            content_type=ContentType.objects.get_for_model(document)
        )

    assert len(comments_for_document(document)) == 5
    document.delete()
    assert len(comments_for_document(document)) == 0


@pytest.mark.django_db
def test_delete_paragraph(paragraph, comment_factory):
    for i in range(5):
        comment_factory(content_object=paragraph)
    comment_count = comments_models.Comment.objects.all().count()
    assert comment_count == len(paragraph.comments.all())

    assert comment_count == 5

    paragraph.delete()
    comment_count = comments_models.Comment.objects.all().count()
    assert comment_count == 0


@pytest.mark.django_db
def test_clusterd_comments_property(paragraph_factory,
                                    document_factory,
                                    comment_factory):

    document = document_factory()
    p1 = paragraph_factory(document=document)
    p2 = paragraph_factory(document=document)

    c1 = comment_factory(content_object=document)
    comment_factory(content_object=c1)
    c2 = comment_factory(content_object=p1)
    c3 = comment_factory(content_object=p2)
    comment_factory(content_object=c2)
    comment_factory(content_object=c3)

    count = comments_models.Comment.objects.all().count()

    assert count == document.clustered_comments.count()
