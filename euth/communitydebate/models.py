from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse

from adhocracy4.categories.fields import CategoryField
from adhocracy4.comments import models as comment_models
from adhocracy4.images import fields
from adhocracy4.models import query
from adhocracy4.modules import models as module_models
from adhocracy4.ratings import models as rating_models


class TopicQuerySet(query.RateableQuerySet, query.CommentableQuerySet):
    pass


class Topic(module_models.Item):
    slug = AutoSlugField(populate_from='name', unique=True)
    name = models.CharField(max_length=120)
    description = RichTextField()
    image = fields.ConfiguredImageField(
        'idea_image',
        upload_to='communitydebate/images',
        blank=True,
    )
    ratings = GenericRelation(rating_models.Rating,
                              related_query_name='topic',
                              object_id_field='object_pk')
    comments = GenericRelation(comment_models.Comment,
                               related_query_name='topic',
                               object_id_field='object_pk')
    category = CategoryField()

    objects = TopicQuerySet.as_manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('topic-detail', args=[str(self.slug)])
