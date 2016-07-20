import os
import pytest

from django.conf import settings
from django.core.urlresolvers import reverse

from euth.organisations import models


@pytest.mark.django_db
def test_absolute_url(organisation):
    url = reverse('organisation-detail', kwargs={'slug': organisation.slug})
    assert organisation.get_absolute_url() == url


@pytest.mark.django_db
def test_natural_keys(organisation):
    assert models.Organisation.objects.get_by_natural_key(
        organisation.name) == organisation


@pytest.mark.django_db
def test_image_validation_image_too_small(organisation_factory, smallImage):
    organisation = organisation_factory(image=smallImage, logo=smallImage)
    with pytest.raises(Exception) as e:
        organisation.full_clean()
    assert 'Image must be at least 600 pixels high' in str(e)


@pytest.mark.django_db
def test_image_big_enough(organisation_factory, bigImage):
    organisation = organisation_factory(image=bigImage, logo=bigImage)
    assert organisation.full_clean() is None


@pytest.mark.django_db
def test_image_validation_type_not_allowed(organisation_factory, ImageBMP):
    organisation = organisation_factory(image=ImageBMP, logo=ImageBMP)
    with pytest.raises(Exception) as e:
        organisation.full_clean()
    assert 'Unsupported file format.' in str(e)


@pytest.mark.django_db
def test_image_validation_image_type_allowed(organisation_factory, ImagePNG):
    organisation = organisation_factory(image=ImagePNG, logo=ImagePNG)
    assert organisation.full_clean() is None


@pytest.mark.django_db
def test_delete_organisation(organisation_factory, ImagePNG):
    organisation = organisation_factory(image=ImagePNG, logo=ImagePNG)
    image_path = os.path.join(settings.MEDIA_ROOT, organisation.image.path)
    logo_path = os.path.join(settings.MEDIA_ROOT, organisation.logo.path)
    assert os.path.isfile(image_path)
    assert os.path.isfile(logo_path)
    count = models.Organisation.objects.all().count()
    assert count == 1
    organisation.delete()
    assert not os.path.isfile(image_path)
    assert not os.path.isfile(logo_path)
    count = models.Organisation.objects.all().count()
    assert count == 0
