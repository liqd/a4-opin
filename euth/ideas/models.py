from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from adhocracy4.ratings import models as rating_models
from contrib.transforms import html_transforms
from euth.comments import models as comment_models
from euth.contrib import validators
from euth.modules import models as module_models


class IdeaQuerySet(models.QuerySet):

    def _rate_value_condition(self, value):
        return models.Case(
            models.When(ratings__value=value, then=models.F('ratings__id')),
            output_field=models.IntegerField()
        )

    def annotate_positive_rating_count(self):
        return self.annotate(
            positive_rating_count=models.Count(
                self._rate_value_condition(1),
                distinct=True  # needed to combine with other count annotations
            )
        )

    def annotate_negative_rating_count(self):
        return self.annotate(
            negative_rating_count=models.Count(
                self._rate_value_condition(-1),
                distinct=True  # needed to combine with other count annotations
            )
        )

    def annotate_comment_count(self):
        return self.annotate(
            comment_count=models.Count(
                'comments',
                distinct=True  # needed to combine with other count annotations
            )
        )


class Idea(module_models.Item):
    slug = AutoSlugField(populate_from='name', unique=True)
    name = models.CharField(max_length=120)
    description = RichTextField()
    image = models.ImageField(upload_to='ideas/images', blank=True,
                              validators=[validators.validate_idea_image])
    ratings = GenericRelation(rating_models.Rating,
                              related_query_name='idea',
                              object_id_field='object_pk')
    comments = GenericRelation(comment_models.Comment,
                               related_query_name='idea',
                               object_id_field='object_pk')

    objects = IdeaQuerySet.as_manager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.description = html_transforms.clean_html_field(
            self.description)
        super(Idea, self).save(*args, **kwargs)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('idea-detail', args=[str(self.slug)])
