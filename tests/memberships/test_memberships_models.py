import pytest
from django.core import mail

from euth.memberships import models


@pytest.mark.django_db
def test_request_membership(project, user):
    request = models.Request.objects.request_membership(project, user)
    assert bool(models.Request.objects.filter(pk=request.pk))
    assert len(mail.outbox) == 1
    subject = (
        'A user requested memberhip to your private project on '
        'example.com'
    )
    assert mail.outbox[0].subject == subject
    assert mail.outbox[0].to == [project.moderators.first().email]


@pytest.mark.django_db
def test_request_decline(membership_request):
    request = membership_request
    request.decline()
    assert not bool(models.Request.objects.filter(pk=request.pk))
    assert request.creator not in request.project.participants.all()


@pytest.mark.django_db
def test_request_accept(membership_request):
    request = membership_request
    project = request.project
    request.accept()
    assert not bool(models.Request.objects.filter(pk=request.pk))
    assert request.creator in project.participants.all()
    assert len(mail.outbox) == 1
    subject = 'Your membership request on example.com was accepted'
    assert mail.outbox[0].subject == subject.format(name=project.name)


@pytest.mark.django_db
def test_invite_email(project, user):
    email = 'test@irgendwogehtesschonhin.de'
    invite = models.Invite.objects.invite(user, project, email)
    assert len(mail.outbox) == 1
    subject = 'You have been invited to join {name} on example.com'
    message = mail.outbox[0]
    assert message.subject == subject.format(name=project.name)
    assert message.to == [email]
    invite_url = 'https://example.com/en/memberships/invites/{}'
    assert invite_url.format(invite.token) in message.body


@pytest.mark.django_db
def test_invate_accept(invite, user):
    invite.accept(user)
    assert not bool(models.Invite.objects.filter(pk=invite.pk))
    assert user in invite.project.participants.all()


@pytest.mark.django_db
def test_invate_reject(invite, user):
    invite.reject()
    assert not bool(models.Invite.objects.filter(pk=invite.pk))
    assert user not in invite.project.participants.all()
