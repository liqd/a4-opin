import magic
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_file_type_and_size(upload):

    file_max_mb = 5
    max_size = file_max_mb*10**6
    fileformats = ('image/png', 'image/jpeg', 'application/pdf')

    errors = []

    filetype = magic.from_buffer(upload.read(), mime=True)
    if filetype.lower() not in fileformats:
        msg = _(
            'Unsupported file format. Supported formats are {}.'.format(
                ', '.join(fileformats)
            )
        )
        errors.append(ValidationError(msg))
    if upload.size > max_size:
        msg = _('File should be at most {} MB'.format(file_max_mb))
        errors.append(ValidationError(msg))
    if errors:
        raise ValidationError(errors)
    return upload
