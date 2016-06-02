from django.conf.urls import include, url
from rest_framework import routers
from .api import CommentViewSet

router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet, base_name='comments_api')

urlpatterns = [
    url(r'^', include(router.urls)),
]