from datetime import timedelta

import pytest
from dateutil.parser import parse
from django.core import mail
from django.core.management import call_command
from freezegun import freeze_time

from euth.actions.models import Action


@pytest.mark.django_db
def test_no_notification_if_flag_is_not_set(
        user_factory, idea_factory, comment_factory):
    user = user_factory(get_notifications=False)
    user2 = user_factory()
    idea = idea_factory(creator=user)

    action_count = Action.objects.all().count()
    assert action_count == 1

    comment_factory(content_object=idea, creator=user2)

    action_count = Action.objects.all().count()
    assert action_count == 2
    assert len(mail.outbox) == 1


@pytest.mark.django_db
def test_idea_creator_gets_email_after_comment(
        user_factory, idea_factory, comment_factory):
    user = user_factory()
    user2 = user_factory()
    idea = idea_factory(creator=user)

    comment_factory(content_object=idea, creator=user2)

    action_count = Action.objects.all().count()
    assert action_count == 2
    assert len(mail.outbox) == 2
    assert 'A Comment was added to your idea' in mail.outbox[1].subject


@pytest.mark.django_db
def test_document_creator_gets_email_after_comment(
        user_factory, document_factory, comment_factory):
    user = user_factory()
    user2 = user_factory()
    document = document_factory(creator=user)

    comment_factory(content_object=document, creator=user2)

    action_count = Action.objects.all().count()
    assert action_count == 1
    assert len(mail.outbox) == 1
    assert 'A Comment was added to your document' in mail.outbox[0].subject


@pytest.mark.django_db
def test_document_creator_gets_email_after_comment_on_paragraph(
        user_factory, document_factory, paragraph_factory, comment_factory):
    user = user_factory()
    user2 = user_factory()
    document = document_factory(creator=user)
    paragraph = paragraph_factory(document=document)

    comment_factory(content_object=paragraph, creator=user2)

    action_count = Action.objects.all().count()
    assert action_count == 1
    assert len(mail.outbox) == 1
    assert 'A Comment was added to your paragraph' in mail.outbox[0].subject


@pytest.mark.django_db
def test_comment_creator_gets_email_after_comment(
        user_factory, idea_factory, comment_factory):
    user = user_factory()
    user2 = user_factory()
    idea = idea_factory(creator=user)

    comment = comment_factory(content_object=idea, creator=user2)
    comment_factory(content_object=comment, creator=user)

    action_count = Action.objects.all().count()

    assert action_count == 4
    assert len(mail.outbox) == 3
    assert 'A Comment was added to your idea' in mail.outbox[1].subject
    assert mail.outbox[1].recipients() == [user.email]
    assert 'A Comment was added to your Comment' in mail.outbox[2].subject
    assert mail.outbox[2].recipients() == [user2.email]


@pytest.mark.django_db
def test_comment_creator_gets_no_email_after_comment_on_own_resource(
        user_factory, idea_factory, comment_factory):
    user = user_factory()
    idea = idea_factory(creator=user)

    comment_factory(content_object=idea, creator=user)

    action_count = Action.objects.all().count()
    assert action_count == 2
    assert len(mail.outbox) == 1


@pytest.mark.django_db
def test_moderator_self_notification(project, module, idea_factory):
    project = module.project
    idea = idea_factory(module=module, creator=project.moderators.first())
    action = Action.objects.get(project=project)
    assert action.target == project
    assert action.action_object == idea
    assert len(mail.outbox) == 0


@pytest.mark.django_db
def test_moderator_notification(project, user, module, idea_factory):
    project = module.project
    idea = idea_factory(module=module, creator=user)
    action = Action.objects.filter(project=project).last()
    assert action.target == project
    assert action.action_object == idea
    assert len(mail.outbox) == 1
    assert mail.outbox[0].to == [project.moderators.first().email]


@pytest.mark.django_db
def test_24_hour_script(
        phase_factory, user_factory, follow_factory):
    user = user_factory()
    user2 = user_factory()
    user3 = user_factory()
    user4 = user_factory(get_notifications=False)

    phase = phase_factory(
        start_date=parse('2013-01-01 17:00:00 UTC'),
        end_date=parse('2013-01-01 18:00:00 UTC')
    )

    project = phase.module.project

    follow_factory(project=project, creator=user)
    follow_factory(project=project, creator=user2)
    follow_factory(project=project, creator=user3, enabled=False)
    follow_factory(project=project, creator=user4)

    action_count = Action.objects.all().count()
    assert action_count == 0

    with freeze_time('2013-01-01 17:30:00 UTC'):
        call_command('notify_followers')
        action_count = Action.objects.all().count()
        assert action_count == 1
        assert len(mail.outbox) == 2
        assert mail.outbox[0].recipients() == [user.email]
        assert mail.outbox[1].recipients() == [user2.email]

        call_command('notify_followers')
        action_count = Action.objects.all().count()
        assert action_count == 1
        assert len(mail.outbox) == 2


@pytest.mark.django_db
def test_24_hour_script_adds_action_for_next_phase(
        phase_factory, user_factory, follow_factory):
    user = user_factory()

    phase1 = phase_factory(
        start_date=parse('2013-01-01 17:00:00 UTC'),
        end_date=parse('2013-01-01 18:00:00 UTC')
    )

    phase2 = phase_factory(
        module=phase1.module,
        start_date=parse('2013-02-02 17:00:00 UTC'),
        end_date=parse('2013-02-02 18:00:00 UTC')
    )

    phase3 = phase_factory(
        module=phase1.module,
        start_date=parse('2013-02-02 18:01:00 UTC'),
        end_date=parse('2013-02-02 19:00:00 UTC')
    )

    project = phase1.module.project

    follow_factory(project=project, creator=user)

    action_count = Action.objects.all().count()
    assert action_count == 0

    # first phase ends within 24 h
    with freeze_time(phase1.end_date - timedelta(hours=1)):
        call_command('notify_followers')
        action_count = Action.objects.all().count()
        assert action_count == 1
        assert len(mail.outbox) == 1
        assert mail.outbox[0].recipients() == [user.email]

    # second phase ends within 24 h
    with freeze_time(phase2.end_date - timedelta(hours=1)):
        call_command('notify_followers')
        action_count = Action.objects.all().count()
        assert action_count == 2
        assert len(mail.outbox) == 2
        assert mail.outbox[0].recipients() == [user.email]

    # second phase ends within 24 h but script has already run
    with freeze_time(phase2.end_date - timedelta(hours=1)):
        call_command('notify_followers')
        action_count = Action.objects.all().count()
        assert action_count == 2
        assert len(mail.outbox) == 2
        assert mail.outbox[0].recipients() == [user.email]

    # third phase ends within 24 h but script has already run
    with freeze_time(phase3.start_date):
        call_command('notify_followers')
        action_count = Action.objects.all().count()
        assert action_count == 3
        assert len(mail.outbox) == 3
        assert mail.outbox[0].recipients() == [user.email]


@pytest.mark.django_db
def test_notify_followers_after_idea_was_added(
        user_factory, idea_factory, follow_factory, module):
    user1 = user_factory()
    user2 = user_factory()
    project = module.project
    moderators = project.moderators
    follow_factory(project=module.project, creator=user1)
    idea_factory(module=module, creator=user2)
    assert len(mail.outbox) == moderators.count() + 1
    text = 'An idea in a project you follow was added'
    assert text in mail.outbox[-1].subject
