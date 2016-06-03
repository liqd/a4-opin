import pytest
from datetime import timedelta

from django.http import HttpResponse
from django.utils import timezone
from django.contrib import auth
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

from ..organisations import models as org_models
from .  import models


@pytest.fixture
def moderator():
    moderator = auth.get_user_model().objects.create(
        username='moderator',
        email='moderator@liqd.de', )
    return moderator


@pytest.fixture
def participant():
    participant = auth.get_user_model().objects.create(
        username='process_participant')
    return participant


@pytest.fixture
def organisation(moderator):
    organisation = org_models.Organisation.objects.create(
        name='test',
        slug='test',
        description_why='Thats why!',
        description_how='Thats how!',
        description='This is test!')
    organisation.initiators.add(moderator)
    return organisation


@pytest.fixture
def project(request, organisation, moderator, participant):
    project = models.Project.objects.create(
        organisation=organisation,
        slug='process',
        name='Process',
        description='Discuss discuss discuss!',
    )
    project.moderators.add(moderator)
    project.participants.add(participant)
    return project


@pytest.fixture
def private_project(request, organisation, moderator, participant):
    project = models.Project.objects.create(
        organisation=organisation,
        slug='private_process',
        name='Process (private)',
        description='Discuss discuss discuss!',
        visibility=models.Visibility.private.value,
    )
    project.moderators.add(moderator)
    project.participants.add(participant)
    return project


@pytest.mark.django_db
def test_get_absolute_url(project):
    project_url = reverse('project-detail', args=[project.slug])
    assert project.get_absolute_url() == project_url


@pytest.mark.django_db
def test_get_by_natural_key(project):
    assert project == models.Project.objects.get_by_natural_key(project.name)


@pytest.mark.django_db
def test_visibility(project, private_project):
    assert project.is_public
    assert not private_project.is_public
    assert not project.is_private
    assert private_project.is_private
