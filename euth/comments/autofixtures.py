from django.contrib.contenttypes.models import ContentType

from .models import Comment
from home.models import HomePage
from autofixture import generators, register, AutoFixture

class CommentAutoFixture(AutoFixture):

    homepage_contenttype = ContentType.objects.get(app_label='home', model='homepage')
    homepage_id = HomePage.objects.all().first().pk

    field_values = {
        'content_type': homepage_contenttype,
        'object_pk': homepage_id,
        'is_removed': generators.BooleanGenerator(),
        'is_censored': generators.BooleanGenerator(),
    }

register(Comment, CommentAutoFixture)
