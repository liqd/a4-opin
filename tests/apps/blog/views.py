from django.views.generic import detail

from . import models


class PostDetail(detail.DetailView):
    model = models.Post
