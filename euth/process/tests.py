from datetime import timedelta

from django.test import TestCase
from django.test.client import RequestFactory
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.models import AnonymousUser, User, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError

from .models import Phase, PhaseType, ParticipationModule, Process
from .permissions import permission_required


class ProcessTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def _create_dummy_phase_type(self, order):
        return PhaseType.objects.create(
            name='dummy_phase_type{}'.format(order),
            module_type=ContentType.objects.get_for_model(ParticipationModule),
            order=order,
        )

    def _create_phase(self, phase_type, module,
                      date_start=None, date_end=None):
        return Phase.objects.create(
            title='Discuss',
            description='Do this and that',
            module=module,
            phase_type=phase_type,
            date_start=date_start,
            date_end=date_end,
        )

    def _create_module(self, process, order, phases):
        module = ParticipationModule.objects.create(
            process=process,
            order=order,
        )

        for phase_type, date_start, date_end in phases:
            self._create_phase(phase_type, module, date_start, date_end)

        return module

    def _create_process(self, name, phases):
        moderator = User.objects.create(
            username='process_moderator_' + name
        )
        participant = User.objects.create(
            username='process_participant__' + name
        )
        process = Process.objects.create(
            name=name,
            title='Process ' + name,
            description='Discuss discuss discuss',
        )
        process.moderators.add(moderator)
        process.participants.add(participant)

        module = self._create_module(process, 1, phases)
        return process

    def test_process_get_current_phase(self):
        phase_type1 = self._create_dummy_phase_type(1)
        phase_type2 = self._create_dummy_phase_type(2)
        phase_type3 = self._create_dummy_phase_type(3)

        now = timezone.now()

        process = self._create_process('open-active-phase', [
            (phase_type1, now - timedelta(2), now - timedelta(1)),
            (phase_type2, now - timedelta(1), None),
            (phase_type3, now + timedelta(1), now + timedelta(2))
        ])
        self.assertEqual(
            process.get_current_phase(now).phase_type,
            phase_type2)

        process = self._create_process('closed-active-phase', [
            (phase_type1, now - timedelta(2), now - timedelta(1)),
            (phase_type2, now - timedelta(1), now + timedelta(1)),
            (phase_type3, now + timedelta(1), now + timedelta(2))
        ])
        self.assertEqual(
            process.get_current_phase(now).phase_type,
            phase_type2)

        process = self._create_process('all-open-nextphase', [
            (phase_type1, now - timedelta(2), now - timedelta(1)),
            (phase_type2, now - timedelta(1), None),
            (phase_type3, None, None)
        ])
        self.assertEqual(
            process.get_current_phase(now).phase_type,
            phase_type2)

        process = self._create_process('phase-starting-now', [
            (phase_type1, now - timedelta(2), now - timedelta(1)),
            (phase_type2, now, None),
            (phase_type3, None, None)
        ])
        self.assertEqual(
            process.get_current_phase(now).phase_type,
            phase_type2)

        process = self._create_process('phase-ending-now', [
            (phase_type1, now - timedelta(2), now - timedelta(1)),
            (phase_type2, now - timedelta(1), now),
            (phase_type3, now, None)
        ])
        self.assertEqual(process.get_current_phase(now).phase_type,
                         phase_type3)

    def test_permission_required_decorator(self):
        phase_type4 = self._create_dummy_phase_type(4)
        content_type = ContentType.objects.get_for_model(User)
        permission = Permission.objects.create(
            codename='moderator_can_test',
            name='A moderator permission for tests',
            content_type=content_type,
        )
        phase_type4.moderator_permissions.add(permission)

        now = timezone.now()
        process = self._create_process('permission-moderator-check', [
            (phase_type4, now - timedelta(1), None)
        ])

        @permission_required('moderator_can_test')
        def wrapped(request, process_name):
            return HttpResponse(status=204)

        request = self.factory.get('/')
        request.user = process.moderators.first()
        response = wrapped(request, process_name='permission-moderator-check')
        self.assertEqual(response.status_code, 204)

        request = self.factory.get('/')
        request.user = process.participants.first()
        response = wrapped(request, process_name='permission-moderator-check')
        self.assertEqual(response.status_code, 403)

        request = self.factory.get('/')
        request.user = AnonymousUser()
        response = wrapped(request, process_name='permission-moderator-check')
        self.assertEqual(response.status_code, 403)

    def test_phase_dont_overlapp(self):
        phase_type5 = self._create_dummy_phase_type(5)
        phase_type6 = self._create_dummy_phase_type(6)
        now = timezone.now()

        process = self._create_process('closed-phases-overlap', [
            (phase_type5, now - timedelta(2), None),
            (phase_type6, now - timedelta(1), None),
        ])
        phase = Phase.objects.get(module__process=process,
                                  phase_type=phase_type6)

        try:
            phase.full_clean()
            self.fail('both phases are currently active')
        except ValidationError as e:
            pass

        process = self._create_process('phase-starts-before-end', [
            (phase_type5, now - timedelta(2), now),
            (phase_type6, now - timedelta(1), None),
        ])
        phase = Phase.objects.get(module__process=process,
                                  phase_type=phase_type6)
        try:
            phase.full_clean()
            self.fail('new phase starts before old ended')
        except ValidationError as e:
            pass

        process = self._create_process('phase-includes-other-phase', [
            (phase_type5, now - timedelta(1), now + timedelta(1)),
            (phase_type6, now - timedelta(2), now + timedelta(2)),
        ])
        phase = Phase.objects.get(module__process=process,
                                  phase_type=phase_type6)
        try:
            phase.full_clean()
            self.fail('phase includes other phase')
        except ValidationError as e:
            pass

        process = self._create_process('phase-overlaps', [
            (phase_type5, now - timedelta(2), now),
            (phase_type6, now - timedelta(1), now + timedelta(1)),
        ])
        phase = Phase.objects.get(module__process=process,
                                  phase_type=phase_type6)
        try:
            phase.full_clean()
            self.fail('phase includes other phase')
        except ValidationError as e:
            pass

    def test_phase_valid(self):
        phase_type7 = self._create_dummy_phase_type(7)
        now = timezone.now()

        process = self._create_process('phase-zero-length', [
            (phase_type7, now, now),
        ])
        phase = Phase.objects.get(module__process=process,
                                  phase_type=phase_type7)
        try:
            phase.full_clean()
        except ValidationError:
            pass

        process = self._create_process('phase-missing-start', [
            (phase_type7, None, now),
        ])
        phase = Phase.objects.get(module__process=process,
                                  phase_type=phase_type7)
        try:
            phase.full_clean()
        except ValidationError:
            pass
