import pytest
from django.urls import reverse

from adhocracy4.comments.models import Comment
from adhocracy4.projects.enums import Access
from euth.exports import mixins
from tests.helpers import redirect_target


@pytest.mark.django_db
def test_paragraph_detail_view(client, paragraph):
    url = reverse('paragraph-detail', kwargs={
        'pk': paragraph.pk
    })

    response = client.get(url)
    response.status_code == 200


@pytest.mark.django_db
def test_paragraph_private_detail_view(client, paragraph_factory, user):
    paragraph = paragraph_factory(
        document__module__project__access=Access.PRIVATE)

    url = reverse('paragraph-detail', kwargs={
        'pk': paragraph.pk
    })

    response = client.get(url)
    redirect_target(response) == 'login'

    client.login(username=user.email, password='password')
    response = client.get(url)
    response.status_code = 403

    paragraph.project.participants.add(user)
    response = client.get(url)
    response.status_code = 200


@pytest.mark.django_db
def test_user_generated_content_mixin(comment_factory, document):
    mixin = mixins.UserGeneratedContentExportMixin()

    virtual = mixin.get_virtual_fields({})
    assert 'creator' in virtual
    assert 'created' in virtual

    comment = comment_factory(content_object=document)

    assert Comment.objects.count() == 1

    assert mixin.get_creator_data(comment) == comment.creator.username
    assert mixin.get_created_data(comment) == comment.created.isoformat()


@pytest.mark.django_db
def test_reply_to_mixin(comment_factory, document):
    mixin = mixins.ItemExportWithRepliesToMixin()

    virtual = mixin.get_virtual_fields({})
    assert 'replies_to' in virtual

    comment = comment_factory(content_object=document)
    reply_comment = comment_factory(content_object=comment)

    assert Comment.objects.count() == 2

    assert mixin.get_replies_to_data(comment) == ''
    assert mixin.get_replies_to_data(reply_comment) == comment.id


@pytest.mark.django_db
def test_export_with_comments(client,
                              paragraph_factory,
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

    module = document.module

    url = '/dashboard/modules/{}/export/0/'.format(module.slug)
    response = client.get(url)
    response.status_code = 403

    user = module.project.moderators.first()

    client.login(username=user.email, password='password')

    response = client.get(url)
    response.status_code = 200


@pytest.mark.django_db
def test_export_without_document(client, module):

    url = '/dashboard/modules/{}/export/0/'.format(module.slug)
    response = client.get(url)
    response.status_code = 403

    user = module.project.moderators.first()

    client.login(username=user.email, password='password')

    response = client.get(url)
    response.status_code = 200
