from rest_framework import routers
from .api import CommentViewset

router = routers.DefaultRouter()
router.register(r'bezirke', CommentViewset, base_name='bezirk')