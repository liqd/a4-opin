import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse

from adhocracy4.models import base
from adhocracy4.projects import models as prj_models

from . import emails


class InviteManager(models.Manager):
    def invite(self, creator, project, email):
        invite = super().create(project=project, creator=creator, email=email)
        emails.InviteEmail.send(invite)
        return invite


class Invite(base.TimeStampedModel):
    """
    An invite to join a privte project.
    """
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        prj_models.Project,
        on_delete=models.CASCADE
    )
    email = models.EmailField()
    token = models.UUIDField(default=uuid.uuid4, unique=True)

    objects = InviteManager()

    class Meta:
        unique_together = ('email', 'project')

    def __str__(self):
        return 'Invite to {s.project} for {s.email}'.format(s=self)

    def get_absolute_url(self):
        url_kwargs = {'invite_token': self.token}
        return reverse('membership-invite-detail', kwargs=url_kwargs)

    def accept(self, user):
        self.project.participants.add(user)
        self.delete()

    def reject(self):
        self.delete()


class RequestManager(models.Manager):
    def request_membership(self, project, user):
        request = super().create(creator=user, project=project)
        emails.RequestReceivedEmail.send(request)
        return request


class Request(base.UserGeneratedContentModel):
    """
    A request for joining a private project.
    """
    project = models.ForeignKey(
        prj_models.Project,
        on_delete=models.CASCADE
    )

    objects = RequestManager()

    class Meta:
        unique_together = ('creator', 'project')

    def __str__(self):
        return 'Request by {s.creator} for {s.project}'.format(s=self)

    def accept(self):
        self.project.participants.add(self.creator)
        self.delete()
        emails.RequestAcceptedEmail.send(self)

    def decline(self):
        self.delete()
        emails.RequestDeniedEmail.send(self)
