import pytest
from django.core import mail

from euth.actions.models import Action


@pytest.mark.django_db
def test_idea_creator_gets_email_after_comment(
        user_factory, idea_factory, document_factory,
        paragraph_factory, comment_factory):

    user = user_factory(get_notifications=False)
    user2 = user_factory()
    idea = idea_factory(creator=user)

    action_count = Action.objects.all().count()
    assert action_count == 0

    comment_factory(content_object=idea, creator=user2)

    action_count = Action.objects.all().count()
    assert action_count == 1
    assert len(mail.outbox) == 0
    user.get_notifications = True
    user.save()

    comment_factory(content_object=idea, creator=user2)

    action_count = Action.objects.all().count()
    assert action_count == 2
    assert len(mail.outbox) == 1
    assert 'A Comment was added to your idea' in mail.outbox[0].subject

    document = document_factory(creator=user)
    paragraph = paragraph_factory(document=document)

    document_comment = comment_factory(content_object=document, creator=user2)
    comment_factory(
        content_object=paragraph, creator=user2)

    action_count = Action.objects.all().count()
    assert action_count == 4
    assert len(mail.outbox) == 3
    assert 'A Comment was added to your document' in mail.outbox[1].subject
    assert 'A Comment was added to your paragraph' in mail.outbox[2].subject

    comment_factory(content_object=document_comment, creator=user2)

    action_count = Action.objects.all().count()
    assert action_count == 5
    assert len(mail.outbox) == 4
    assert 'A Comment was added to your Comment' in mail.outbox[3].subject
