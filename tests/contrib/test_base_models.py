import freezegun
import pytest
from django.utils import timezone


@pytest.mark.django_db
def test_time_stamped_model(time_stamped_model):
    with freezegun.freeze_time('2016-06-06 12:00:00'):
        obj = time_stamped_model()
        assert obj.pk is None
        assert obj.created == timezone.now()
        assert obj.modified is None
        obj.save()
        assert obj.pk is not None
        assert obj.created == timezone.now()
        assert obj.modified is None
    with freezegun.freeze_time('2016-06-06 12:05:00'):
        obj.save()
        assert obj.created < timezone.now()
        assert obj.modified == timezone.now()
