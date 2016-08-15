import pytest
from django.contrib.contenttypes.models import ContentType
from django.core import mail
from django.core.urlresolvers import reverse
from rest_framework import status


@pytest.mark.django_db
def test_anonymous_user_can_not_report(apiclient):
    url = reverse('reports-list')
    data = {}
    response = apiclient.post(url, data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_anonymous_user_can_not_view_reportlist(apiclient):
    url = reverse('reports-list')
    response = apiclient.get(url, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_authenticated_user_can_report(apiclient, user):
    apiclient.force_authenticate(user=user)
    url = reverse('reports-list')
    data = {}
    response = apiclient.post(url, data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_authenticated_user_can_not_view_reportlist(apiclient, user):
    apiclient.force_authenticate(user=user)
    url = reverse('reports-list')
    response = apiclient.get(url, format='json')
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_authenticated_user_can_post(apiclient, user, comment, admin):
    apiclient.force_authenticate(user=user)
    url = reverse('reports-list')
    comments_ct = ContentType.objects.get(
        app_label="comments", model="comment")
    data = {
        'content_type': comments_ct.pk,
        'object_pk': comment.pk,
        'description': 'This comment sucks'
    }
    response = apiclient.post(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['description'] == 'This comment sucks'
    assert len(mail.outbox) == 2
    assert 'A resource of type \'Comment\' has been reported' in mail.outbox[
        0].subject
    assert 'A Comment that you created' in mail.outbox[
        1].subject
