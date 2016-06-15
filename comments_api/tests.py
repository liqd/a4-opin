from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from rest_framework.test import force_authenticate
from rest_framework import status
from django.contrib.auth.models import AnonymousUser, User, Permission
from django_comments.models import Comment
from django.contrib.contenttypes.models import ContentType

from django.core.urlresolvers import reverse


class CommentTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user1 = self._create_user('user1', 'password')
        self.user2 = self._create_user('user2', 'password')
        self.comment1 = self._create_comment('comment', 1, self.user1)
        self.comment_contenttype = ContentType.objects.get(
            app_label="django_comments", model="comment").pk

    def _create_user(self, name, password):
        user = User.objects.create(
            username=name,
            password=password
        )
        return user

    def _create_comment(self, comment, object_pk, user):
        content_type = ContentType.objects.all()[0]
        comment = Comment.objects.create(
            comment=comment,
            object_pk=object_pk,
            content_type=content_type,
            user=user,
            site_id=1
        )
        return comment

    def test_anonymous_user_can_not_comment(self):
        url = reverse('comments-list')
        data = {}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_can_not_post_invalid_data(self):
        self.client.force_authenticate(user=self.user1)
        url = reverse('comments-list')
        data = {}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_authenticated_user_can_post_valid_data(self):
        self.client.force_authenticate(user=self.user1)
        url = reverse('comments-list')
        data = {
            'comment': 'comment comment',
            'object_pk': 1,
            'content_type': 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_user_can_edit_own_comment(self):
        self.client.force_authenticate(user=self.user1)
        data = {'comment': 'comment comment comment'}
        url = reverse('comments-detail', kwargs={'pk': self.comment1.pk})
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['comment'], 'comment comment comment')

    def test_authenticated_user_can_not_edit_comment_of_other_user(self):
        self.client.force_authenticate(user=self.user2)
        data = {'comment': 'comment comment comment'}
        url = reverse('comments-detail', kwargs={'pk': self.comment1.pk})
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonoymous_user_can_not_edit_comment(self):
        data = {'comment': 'comment comment comment'}
        url = reverse('comments-detail', kwargs={'pk': self.comment1.pk})
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_can_reply_to_comment(self):
        url = reverse('comments-detail', kwargs={'pk': self.comment1.pk})
        response = self.client.get(url)
        self.assertEqual(len(response.data['child_comments']), 0)
        self.client.force_authenticate(user=self.user2)
        url = reverse('comments-list')
        data = {
            'comment': 'comment comment',
            'object_pk': self.comment1.pk,
            'content_type': self.comment_contenttype
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        url = reverse('comments-detail', kwargs={'pk': self.comment1.pk})
        response = self.client.get(url)
        self.assertEqual(len(response.data['child_comments']), 1)
