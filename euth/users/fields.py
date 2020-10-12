from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.forms.fields import Field

from euth.users.forms import User
from euth.users.widgets import UserSearchInput


class UserSearchField(Field):

    def __init__(self, identifier=None, *args, **kwargs):
        self.identifier = identifier
        self.widget = UserSearchInput(identifier=self.identifier)

        super().__init__(*args, **kwargs)

    def to_python(self, value):
        if value:
            try:
                return User.objects.get(username__exact=value)
            except ObjectDoesNotExist:
                raise ValidationError('{} doesn\'t exist.'.format(value))
        return None
