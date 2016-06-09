from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone


class Process(models.Model):
    name = models.CharField(max_length=128, db_index=True, unique=True)
    title = models.CharField(max_length=1024)
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
        return reverse('process-detail', args=[str(self.name)])

    def __str__(self):
        return 'process «{}»'.format(self.name)


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
        return 'phase type «{}.{}»'.format(module_type.model, self.name)


class ParticipationModule(models.Model):

    class Meta:
        unique_together = (("process", "order"),)

    process = models.ForeignKey(
        Process,
        on_delete=models.CASCADE,
    )
    order = models.PositiveSmallIntegerField(db_index=True)


class Phase(models.Model):

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

    def __str__(self):
        return '{} phase of process «{}»'.format(
            quantityStr(self.order), self.process.name)
