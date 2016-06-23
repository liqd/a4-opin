from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.core.exceptions import ValidationError


class Process(models.Model):
    slug = models.SlugField(
        max_length=512,
        db_index=True,
        unique=True,
    )
    title = models.CharField(max_length=512)
    description = models.TextField()
    participants = models.ManyToManyField(
        User,
        related_name="process_participant",
        blank=True,
    )
    moderators = models.ManyToManyField(
        User,
        related_name="process_moderator",
    )

    def get_current_phase(self, now=timezone.now()):
        return Phase.objects.filter(
            models.Q(module__process=self, date_start__lte=now) & (
                models.Q(date_end__exact=None) |
                models.Q(date_end__gt=now)
            )
        ).first()

    def get_absolute_url(self):
        return reverse('process-detail', args=[str(self.slug)])

    def __str__(self):
        return self.slug

    @property
    def phases(self):
        phases = Phase.objects\
                      .filter(module__process=self)\
                      .order_by('module__order', 'phase_type__order')
        return phases


class PhaseType(models.Model):

    class Meta:
        unique_together = (
            ("module_type", "order"),
            ("module_type", "name")
        )

    name = models.CharField(max_length=100)
    module_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField(db_index=True)
    moderator_permissions = models.ManyToManyField(
        Permission,
        related_name="moderator_permissions",
    )
    participant_permissions = models.ManyToManyField(
        Permission,
        related_name="user_permissions",
    )

    def __str__(self):
        return '{}.{}'.format(self.module_type.model, self.name)


class ParticipationModule(models.Model):

    class Meta:
        unique_together = (("process", "order"),)

    process = models.ForeignKey(
        Process,
        on_delete=models.CASCADE,
    )
    order = models.PositiveSmallIntegerField(db_index=True)

    def __str__(self):
        return '{}({}) of {}'.format(self.__class__.__name__, self.order, self.process)


class Phase(models.Model):

    class Meta:
        unique_together = (("phase_type", "module"),)

    title = models.CharField(max_length=1024)
    description = models.TextField()
    module = models.ForeignKey(
        ParticipationModule,
        on_delete=models.CASCADE,
    )
    phase_type = models.ForeignKey(
        PhaseType,
        on_delete=models.CASCADE,
    )
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)

    @property
    def is_open(self):
        return self.date_start and not self.date_end

    @property
    def is_dated(self):
        return self.date_start

    def clean_dates(self):
        if not self.date_start and self.date_end:
            raise ValidationError({ 'date_start': 'phase end requires start' })

        if self.date_end and self.date_start >= self.date_end:
            raise ValidationError({ 'date_end': 'phase end before start' })


    def clean_phases_overlapp(self):
        qs = Phase.objects.filter(
            module__process=self.module.process,
            date_start__isnull=False
        ).exclude(
            pk__exact=self.pk
        )

        for other in qs:
            if self.is_open and other.is_open:
                raise ValidationError({ 'date_end': '{} is also open'.format(other) })
            elif (self.is_open and other.date_end > self.date_start):
                raise ValidationError({ 'date_start': '{} starts after'.format(other) })
            elif (other.is_open and self.date_end > other.date_start):
                raise ValidationError({ 'date_end': '{} starts before'.format(other) })
            elif not (self.date_end <= other.date_start or self.date_start >= other.date_end):
                message = 'overlaps with {}'.format(other)
                raise ValidationError({
                    'date_end': message,
                    'date_start': message,
                })


    def clean_module_constraint(self):
        if self.phase_type.module_type != ContentType.objects.get_for_model(self.module):
            raise ValidationError({
                'phase_type': 'phase_type and module incompatbile',
            })

    def clean(self):
        self.clean_dates()
        if self.is_dated:
            self.clean_phases_overlapp()
        self.clean_module_constraint()


    def __str__(self):
        return '{}({}) of {}'.format(
            self.phase_type, self.module.order, self.module.process)
