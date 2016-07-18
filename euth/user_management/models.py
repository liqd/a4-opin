import uuid

from django.conf import settings
from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils import fields


class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    username = models.CharField(_('username'), max_length=60, unique=True,
        help_text=_('Required. 60 characters or fewer. Letters, digits, spaces and '
                    '@/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(r'^[\w]+[ \w.@+-]*$',
                                      _('Enter a valid username. This value may contain only '
                                        'letters, digits, spaces and @/./+/-/_ characters. It '
                                        'must start with a digit or a letter.'),
                                      'invalid'),
        ],
        error_messages={
            'unique': _('A user with that username already exists.'),
        })
    email = models.EmailField(_('email address'), unique=True,
        error_messages={
            'unique': _('A user with that email address already exists.'),
       })
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = fields.AutoCreatedField()

    objects = auth_models.UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s <%s>' % (self.username, self.email)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.username


class Registration(models.Model):
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    username = models.TextField(max_length=255)
    email = models.EmailField()
    password = models.TextField(max_length=128)
    next_action = models.URLField(blank=True, null=True)


class Reset(models.Model):
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    next_action = models.URLField(blank=True, null=True)
