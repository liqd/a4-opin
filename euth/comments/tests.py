from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from rest_framework import status

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Comment


class CommentTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user1 = self._create_user('user1', 'password')
        self.user2 = self._create_user('user2', 'password')
        self.admin = self._create_user('admin', 'password')
        self.admin.is_superuser = True
        self.admin.save()
        self.comment1 = self._create_comment('comment', 1, self.user1)
        self.comment_contenttype = ContentType.objects.get(
            app_label="comments", model="comment").pk

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
        )
        return comment

    

    
    
    
    
    
    
    
    
    