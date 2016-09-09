import pytest
from django.core import mail

from euth.memberships import models


@pytest.mark.django_db
def test_decline(membership_request):
    request = membership_request
    request.decline()
    assert not bool(models.Request.objects.filter(pk=request.pk))
    assert request.creator not in request.project.participants.all()


@pytest.mark.django_db
def test_accept(membership_request):
    request = membership_request
    project = request.project
    request.accept()
    assert not bool(models.Request.objects.filter(pk=request.pk))
    assert request.creator in project.participants.all()
    assert len(mail.outbox) == 1
    subject = 'Your membership request to {name} accepted'
    assert mail.outbox[0].subject == subject.format(name=project.name)


@pytest.mark.django_db
def test_request_membership(project, user):
    request = models.Request.objects.request_membership(project, user)
    assert bool(models.Request.objects.filter(pk=request.pk))
    assert len(mail.outbox) == 1
    subject = 'Access requested to {name} on example.com'
    assert mail.outbox[0].subject == subject.format(name=project.name)
    assert mail.outbox[0].to == [project.moderators.first().email]
