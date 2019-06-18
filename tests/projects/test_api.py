import pytest
from django.core import mail
from django.urls import reverse
from rest_framework import status

from tests.factories import UserFactory


@pytest.mark.django_db
def test_anonymous_user_cannot_get_project_detail(apiclient, project):
    url = reverse('projects-detail', kwargs={'pk': project.pk})
    response = apiclient.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_authenticated_user_cannot_get_project_detail(apiclient,
                                                      project, user):
    apiclient.force_authenticate(user=user)
    url = reverse('projects-detail', kwargs={'pk': project.pk})
    response = apiclient.get(url)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_initiator_cannot_get_project_detail(apiclient, project):
    initiator = project.organisation.initiators.all().first()
    apiclient.force_authenticate(user=initiator)
    url = reverse('projects-detail', kwargs={'pk': project.pk})
    response = apiclient.get(url)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_initiator_can_add_moderator_to_project(apiclient, project, user):
    initiator = project.organisation.initiators.all().first()
    apiclient.force_authenticate(user=initiator)
    url = reverse('projects-detail', kwargs={'pk': project.pk})
    user1 = UserFactory(username='Cersei')
    data = {
        'moderators': [user1.pk]
    }
    response = apiclient.patch(url, data, format='json')
    assert len(mail.outbox) == 1
    message = 'You were added as a moderator to a project'
    assert message in mail.outbox[0].subject
    assert mail.outbox[0].to[0] == user1.email
    assert response.status_code == status.HTTP_200_OK
