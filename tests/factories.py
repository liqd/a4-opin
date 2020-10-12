from io import BytesIO

import factory
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.core.files import base
from django.core.files import images
from PIL import Image

from adhocracy4.test import factories


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = settings.AUTH_USER_MODEL

    username = factory.Sequence(lambda n: 'user{}'.format(n))
    password = make_password('password')
    email = factory.Sequence(lambda n: 'user{}@liqd.net'.format(n))
    timezone = factory.Faker('timezone')


class AdminFactory(UserFactory):
    is_superuser = True
    is_staff = True


class ContentTypeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'contenttypes.ContentType'

    app_label = factory.Faker('name')
    model = factory.Faker('name')
    name = factory.Faker('name')


class PhaseFactory(factories.PhaseFactory):
    type = 'blog:phase'


class ImageFactory():
    """
    Create a django file object containg an image.
    """

    def __call__(self, resolution, image_format='JPEG', name=None):

        filename = name or 'default.{}'.format(image_format.lower())
        color = 'blue'
        image = Image.new('RGB', resolution, color)
        image_data = BytesIO()
        image.save(image_data, image_format)
        image_content = base.ContentFile(image_data.getvalue())
        return images.ImageFile(image_content.file, filename)
