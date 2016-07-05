from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_image(image, min_width, min_height):
    errors = []
    if image.width < min_width:
        msg = _('Image must be at least {min_width} pixels wide')
        errors += ValidationError(msg.format(min_width=min_width))
    if image.height < min_height:
        msg = _('Image must be at least {min_height} pixels high')
        errors += ValidationError(msg.format(min_height=min_height))
    if errors:
        raise ValidationError(errors)
    return image


def validate_hero_image(image):
    validate_image(image, 1300, 600)


def validate_logo(image):
    validate_image(image, 400, 400)
