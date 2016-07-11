import magic

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

image_max_mb = 5



def validate_image(image, min_width, min_height):
    errors = []

    imagetype = magic.from_buffer(image.read(), mime=True)
    if imagetype.lower() not in settings.ALLOWED_UPLOAD_IMAGES:
        _msg = _("Unsupported file format. Supported formats are %s."
                                          % ", ".join(settings.ALLOWED_UPLOAD_IMAGES))
        errors.append(ValidationError(_msg))
    image_max_size = image_max_mb * 10**6
    if image.size > image_max_size:
        msg = _('Image should be at most {max_size} MB')
        errors.append(ValidationError(msg.format(max_size=image_max_mb)))
    if image.width < min_width:
        msg = _('Image must be at least {min_width} pixels wide')
        errors.append(ValidationError(msg.format(min_width=min_width)))
    if image.height < min_height:
        msg = _('Image must be at least {min_height} pixels high')
        errors.append(ValidationError(msg.format(min_height=min_height)))
    if errors:
        raise ValidationError(errors)
    return image