from rest_framework import routers

from django.conf.urls import include, url

from .api import CommentViewSet

router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet, base_name='comments')

urlpatterns = [
    url(r'^', include(router.urls)),
]
