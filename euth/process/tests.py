import pytest
from datetime import timedelta

from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.models import AnonymousUser, User, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError

from .models import Phase, PhaseType, ParticipationModule, Process
from .permissions import permission_required


@pytest.fixture
def moderator(db):
    moderator, created = User.objects.update_or_create(
        username='moderator',
        email='moderator@liqd.de', )
    return moderator


@pytest.fixture
def participant(db):
    participant, created = User.objects.update_or_create(
        username='process_participant')
    return participant


@pytest.fixture
def process(request, db, moderator, participant):
    if request.cls:
        name = request.cls.__name__ + "." + request.function.__name__
    else:
        name = request.function.__name__
    process = Process.objects.create(slug=name,
                                     title='Process ' + name,
                                     description='Discuss discuss discuss', )
    process.moderators.add(moderator)
    process.participants.add(participant)
    ParticipationModule.objects.create(process=process,
                                       order=1, )
    return process


def phase_type(order):
    phase_type, created = PhaseType.objects.update_or_create(
        name='dummy_phase_type{}'.format(order),
        module_type=ContentType.objects.get_for_model(ParticipationModule),
        order=order, )
    return phase_type


@pytest.fixture
def phase_type1(db):
    return phase_type(1)


@pytest.fixture
def phase_type2(db):
    return phase_type(2)


@pytest.fixture
def phase_type3(db):
    return phase_type(3)


def add_phases(process, phases):
    module = process.participationmodule_set.first()
    for phase_type, date_start, date_end in phases:
        Phase.objects.create(title='Discuss',
                             description='Do this and that',
                             module=module,
                             phase_type=phase_type,
                             date_start=date_start,
                             date_end=date_end, )


def test_current_open_active_phase(process, phase_type1, phase_type2,
                                   phase_type3):
    now = timezone.now()
    add_phases(process, [
        (phase_type1, now - timedelta(2), now - timedelta(1)),
        (phase_type2, now - timedelta(1), now + timedelta(1)),
        (phase_type3, now + timedelta(1), now + timedelta(2))
    ])
    assert process.get_current_phase(now).phase_type == phase_type2


def test_current_closed_active_phase(process, phase_type1, phase_type2,
                                     phase_type3):
    now = timezone.now()
    add_phases(process, [
        (phase_type1, now - timedelta(2), now - timedelta(1)),
        (phase_type2, now - timedelta(1), now + timedelta(1)),
        (phase_type3, now + timedelta(1), now + timedelta(2))
    ])

    assert process.get_current_phase(now).phase_type == phase_type2


def test_current_all_open_nextphase(process, phase_type1, phase_type2,
                                    phase_type3):
    now = timezone.now()
    add_phases(process, [
        (phase_type1, now - timedelta(2), now - timedelta(1)),
        (phase_type2, now - timedelta(1), None), (phase_type3, None, None)
    ])
    assert process.get_current_phase(now).phase_type == phase_type2


def test_current_phase_starting_now(process, phase_type1, phase_type2,
                                    phase_type3):
    now = timezone.now()
    add_phases(process, [
        (phase_type1, now - timedelta(2), now - timedelta(1)),
        (phase_type2, now, None), (phase_type3, None, None)
    ])
    assert process.get_current_phase(now).phase_type == phase_type2


def test_current_phase_ending_now(process, phase_type1, phase_type2,
                                  phase_type3):
    now = timezone.now()
    add_phases(process, [
        (phase_type1, now - timedelta(2), now - timedelta(1)),
        (phase_type2, now - timedelta(1), now), (phase_type3, now, None)
    ])
    assert process.get_current_phase(now).phase_type == phase_type3


def test_current_phase_none(process, phase_type1, phase_type2, phase_type3):
    now = timezone.now()
    add_phases(process, [
        (phase_type1, now - timedelta(3), now - timedelta(2)),
        (phase_type2, now - timedelta(2), now - timedelta(1)),
        (phase_type3, now + timedelta(1), None)
    ])
    assert process.get_current_phase(now) == None


def test_phase_validation_overlap(process, phase_type1, phase_type2):
    now = timezone.now()

    add_phases(process, [
        (phase_type1, now - timedelta(2), None),
        (phase_type2, now - timedelta(1), None),
    ])

    phase = Phase.objects.get(module__process=process, phase_type=phase_type2)

    with pytest.raises(ValidationError):
        phase.full_clean()


def test_phase_validation_start_before_end(process, phase_type1, phase_type2):
    now = timezone.now()

    add_phases(process, [
        (phase_type1, now - timedelta(2), now),
        (phase_type2, now - timedelta(1), None),
    ])

    phase = Phase.objects.get(module__process=process, phase_type=phase_type2)

    with pytest.raises(ValidationError):
        phase.full_clean()


def test_phase_includes_other_phase(process, phase_type1, phase_type2):
    now = timezone.now()

    add_phases(process, [
        (phase_type1, now - timedelta(1), now + timedelta(1)),
        (phase_type2, now - timedelta(2), now + timedelta(2)),
    ])

    phase = Phase.objects.get(module__process=process, phase_type=phase_type2)

    with pytest.raises(ValidationError):
        phase.full_clean()


def test_phase_overlaps(process, phase_type1, phase_type2):
    now = timezone.now()

    add_phases(process, [
        (phase_type1, now - timedelta(2), now),
        (phase_type2, now - timedelta(1), now + timedelta(1))
    ])

    phase = Phase.objects.get(module__process=process, phase_type=phase_type2)

    with pytest.raises(ValidationError):
        phase.full_clean()


def test_permission_required_decorator(rf, process, phase_type1):
    now = timezone.now()
    content_type = ContentType.objects.get_for_model(User)
    permission = Permission.objects.create(
        codename='moderator_can_test',
        name='A moderator permission for tests',
        content_type=content_type, )
    phase_type1.moderator_permissions.add(permission)

    add_phases(process, [(phase_type1, now - timedelta(1), None)])

    @permission_required('moderator_can_test')
    def wrapped(request, process_slug):
        return HttpResponse(status=204)

    request = rf.get('/')
    request.user = process.moderators.first()
    response = wrapped(request, process_slug=process.slug)

    assert response.status_code == 204

    request = rf.get('/')
    request.user = process.participants.first()
    response = wrapped(request, process_slug=process.slug)
    assert response.status_code == 403

    request = rf.get('/')
    request.user = AnonymousUser()
    response = wrapped(request, process_slug=process.slug)
    assert response.status_code == 403


def test_phase_valid(process, phase_type1):
    now = timezone.now()

    add_phases(process, [(phase_type1, now, now), ])
    phase = Phase.objects.get(module__process=process, phase_type=phase_type1)

    with pytest.raises(ValidationError):
        phase.full_clean()


def test_phase_missing_start(process, phase_type1):
    now = timezone.now()

    add_phases(process, [(phase_type1, None, now), ])
    phase = Phase.objects.get(module__process=process, phase_type=phase_type1)

    with pytest.raises(ValidationError):
        phase.full_clean()
