from django.db import models
from euth.modules import models as module_models
from euth.contrib import validators


class Idea(module_models.Item):
    slug = models.SlugField(max_length=512, unique=True)
    name = models.CharField(max_length=512)
    description = models.TextField()
    image = models.ImageField(upload_to='ideas/images', blank=True,
                              validators=[validators.validate_hero_image])

    def __str__(self):
        return self.name
