from django.utils import timezone

import freezegun
import pytest


class TestTimeStampedModel:

    def test_created(self, time_stamped_model):
        with freezegun.freeze_time('2016-06-06'):
            obj = time_stamped_model()
            assert obj.modified is None
            assert obj.created == timezone.now()

    @pytest.mark.django_db
    def test_updated(self, time_stamped_model):
        with freezegun.freeze_time('2016-06-06'):
            obj = time_stamped_model()
            obj.save()
            assert obj.modified is None
            obj.save()
            assert obj.created == obj.modified == timezone.now()
