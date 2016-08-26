from django.views.generic import list

from . import models


class PostList(list.ListView):
    model = models.Post
