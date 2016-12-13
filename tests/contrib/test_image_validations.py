import pytest
from django.core.exceptions import ValidationError

from contrib.validations.image_validations import validate_image


def test_min_size_validation(image_factory):
    with pytest.raises(ValidationError):
        image = image_factory((100, 100), 'JPEG')
        validate_image(image, 50, 101)

    with pytest.raises(ValidationError):
        image = image_factory((100, 100), 'JPEG')
        validate_image(image, 101, 50)

    image = image_factory((100, 100), 'JPEG')
    validate_image(image, 100, 100)


def test_aspect_validation(image_factory):
    square_image = image_factory((100, 109), 'JPEG')
    image = image_factory((100, 120), 'JPEG')

    validate_image(square_image, 100, 100, (1, 1))

    with pytest.raises(ValidationError):
        validate_image(image, 100, 100, (1, 1))
