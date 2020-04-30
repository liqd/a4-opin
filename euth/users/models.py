from datetime import date

from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models
from django.templatetags.static import static
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django_countries import fields as countries_fields
from pytz import common_timezones

from adhocracy4.images import fields
from euth.users import USERNAME_REGEX

USERNAME_INVALID_MESSAGE = _('Enter a valid username. This value may contain '
                             'only letters, digits, spaces and @/./+/-/_ '
                             'characters. It must start with a digit or a '
                             'letter.')
USERNAME_NOT_UNIQUE = _('A user with that username already exists.')
USERNAME_HELP = _('Required. 60 characters or fewer. Letters, digits, spaces '
                  'and @/./+/-/_ only.')
USERNAME_VALIDATOR = validators.RegexValidator(USERNAME_REGEX,
                                               USERNAME_INVALID_MESSAGE,
                                               'invalid')

EMAIL_NOT_UNIQUE = _('A user with that email address already exists.')

IS_STAFF_HELP = _('Designates whether the user can log into this admin site.')
IS_ACTIVE_HELP = _('Designates whether this user should be treated as active. '
                   'Unselect this instead of deleting accounts.')
GET_NOTIFICATIONS_HELP = _('Designates whether yo u want to receive '
                           'notifications. Unselect if you do not '
                           'want to receive notifications.')


class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    username = models.CharField(_('username'),
                                max_length=60, unique=True,
                                help_text=USERNAME_HELP,
                                validators=[USERNAME_VALIDATOR],
                                error_messages={
                                    'unique': _(USERNAME_NOT_UNIQUE),
    })

    email = models.EmailField(_('email address'), unique=True,
                              error_messages={
                                  'unique': EMAIL_NOT_UNIQUE,
    })
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=IS_STAFF_HELP)
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=IS_ACTIVE_HELP)
    date_joined = models.DateTimeField(editable=False, default=timezone.now)

    get_notifications = models.BooleanField(
        verbose_name=_('Send me email notifications'),
        default=True,
        help_text=GET_NOTIFICATIONS_HELP)

    _avatar = fields.ConfiguredImageField(
        'avatar',
        upload_to='users/images',
        blank=True,
        verbose_name=_('Avatar picture'),
    )

    description = models.CharField(
        blank=True,
        max_length=250,
        verbose_name=_('Short description about yourself'),
        help_text=_('Write a little bit about yourself. '
                    '(max. 250 characters)')
    )

    twitter_handle = models.CharField(
        blank=True,
        max_length=15,
        verbose_name=_('Twitter name'),
    )

    facebook_handle = models.CharField(
        blank=True,
        max_length=50,
        verbose_name=_('Facebook name'),
    )

    instagram_handle = models.CharField(
        blank=True,
        max_length=30,
        verbose_name=_('Instagram name'),
    )

    country = countries_fields.CountryField(
        blank=True,
        verbose_name=_('Country of residence'),
    )

    city = models.CharField(
        blank=True,
        max_length=80,
        verbose_name=_('City of residence'),
    )

    birthdate = models.DateField(
        blank=True,
        null=True,
        verbose_name=_('Date of birth'),
    )

    gender = models.CharField(
        blank=True,
        verbose_name=_('Gender'),
        max_length=2,
        choices=[
            ('M', _('Male')),
            ('F', _('Female')),
            ('T', _('Transgender')),
            ('TF', _('Transgender Female')),
            ('TM', _('Transgender Male')),
            ('I', _('Intersex')),
            ('GF', _('Gender Fluid')),
            ('O', _('Other')),
        ],
    )

    languages = models.CharField(
        blank=True,
        verbose_name=_('Languages'),
        max_length=150,
        help_text=_('Enter the languages you’re speaking.')
    )

    timezone = models.CharField(
        blank=True,
        verbose_name=_('Time zone'),
        max_length=100,
        choices=[(t, t) for t in common_timezones]
    )

    objects = auth_models.UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('profile', kwargs={'slug': str(self.username)})

    def __str__(self):
        return self.get_full_name()

    @property
    def has_social_share(self):
        return (
            self.twitter_handle or self.facebook_handle
            or self.instagram_handle
        )

    @property
    def organisations(self):
        return self.organisation_set.all()

    @property
    def avatar(self):
        if self._avatar:
            return self._avatar

    @property
    def avatar_fallback(self):
        id = self.pk % 6
        return static('images/penguin_{}.png'.format(id))

    @property
    def age(self):
        today = date.today()
        years_difference = today.year - self.birthdate.year
        is_before_birthday = (today.month, today.day) < (self.birthdate.month,
                                                         self.birthdate.day)
        elapsed_years = years_difference - int(is_before_birthday)
        return elapsed_years

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s <%s>' % (self.username, self.email)
        return full_name.strip()

    def get_short_name(self):
        """
        Return the short name for the user.
        """
        return self.username

    def signup(self, username, email, timezone, commit=True):
        """Update the fields required for sign-up."""
        self.username = username
        self.email = email
        self.timezone = timezone
        if commit:
            self.save()
