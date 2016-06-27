import pytest

from rest_framework import status
from rest_framework.test import APIClient

from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType

apiclient = APIClient()


@pytest.mark.django_db
def test_anonymous_user_can_not_comment():
    apiclient.force_authenticate(user=None)
    url = reverse('comments-list')
    data = {}
    response = apiclient.post(url, data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_authenticated_user_can_not_post_invalid_data(user):
    apiclient.force_authenticate(user=user)
    url = reverse('comments-list')
    data = {}
    response = apiclient.post(url, data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_authenticated_user_can_post_valid_data(user):
    apiclient.force_authenticate(user=user)
    url = reverse('comments-list')
    data = {
        'comment': 'comment comment',
        'object_pk': 1,
        'content_type': 1
    }
    response = apiclient.post(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_authenticated_user_can_edit_own_comment(comment):
    apiclient.force_authenticate(user=comment.user)
    data = {'comment': 'comment comment comment'}
    url = reverse('comments-detail', kwargs={'pk': comment.pk})
    response = apiclient.patch(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['comment'] == 'comment comment comment'


@pytest.mark.django_db
def test_authenticated_user_can_not_edit_comment_of_other_user(user2, comment):
    apiclient.force_authenticate(user=user2)
    data = {'comment': 'comment comment comment'}
    url = reverse('comments-detail', kwargs={'pk': comment.pk})
    response = apiclient.patch(url, data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_anonymous_user_can_not_edit_comment(comment):
    apiclient.force_authenticate(user=None)
    data = {'comment': 'comment comment comment'}
    url = reverse('comments-detail', kwargs={'pk': comment.pk})
    response = apiclient.patch(url, data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_authenticated_user_can_reply_to_comment(user2, comment):
    comment_contenttype = ContentType.objects.get(
    app_label="comments", model="comment").pk
    url = reverse('comments-detail', kwargs={'pk': comment.pk})
    response = apiclient.get(url)
    assert len(response.data['child_comments']) == 0
    apiclient.force_authenticate(user=user2)
    url = reverse('comments-list')
    data = {
        'comment': 'comment comment',
        'object_pk': comment.pk,
        'content_type': comment_contenttype
    }
    response = apiclient.post(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    url = reverse('comments-detail', kwargs={'pk': comment.pk})
    response = apiclient.get(url)
    assert len(response.data['child_comments']) == 1


@pytest.mark.django_db
def test_anonymous_user_can_not_delete_comment(comment):
    apiclient.force_authenticate(user=None)
    url = reverse('comments-detail', kwargs={'pk': comment.pk})
    response = apiclient.delete(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_authenticated_user_can_not_delete_comment(comment, user2):
    url = reverse('comments-detail', kwargs={'pk': comment.pk})
    apiclient.force_authenticate(user=user2)
    response = apiclient.delete(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_creater_of_comment_can_set_removed_flag(comment, user):
    url = reverse('comments-detail', kwargs={'pk': comment.pk})
    apiclient.force_authenticate(user=user)
    response = apiclient.delete(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['is_deleted'] == True
    assert response.data['comment'] == 'deleted by creator'


@pytest.mark.django_db
def test_admin_of_comment_can_set_censored_flag(comment, admin):
    url = reverse('comments-detail', kwargs={'pk': comment.pk})
    apiclient.force_authenticate(user=admin)
    response = apiclient.delete(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['is_deleted'] == True
    assert response.data['comment'] == 'deleted by moderator'
