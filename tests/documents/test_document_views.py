import pytest
from django.core.urlresolvers import reverse

from adhocracy4.comments.models import Comment
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
    paragraph = paragraph_factory(document__module__project__is_public=False)

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
def test_reply_to_mixin(comment_factory, document):
    mixin = mixins.ItemExportWithRepliesToMixin()

    virtual = mixin.get_virtual_fields({})
    assert 'replies_to' in virtual

    comment = comment_factory(content_object=document)
    reply_comment = comment_factory(content_object=comment)

    assert Comment.objects.count() == 2

    assert mixin.get_replies_to_data(comment) == ''
    assert mixin.get_replies_to_data(reply_comment) == comment.id
