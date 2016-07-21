import freezegun
import pytest
from django.core.management.color import no_style
from django.db import connection
from django.db.models import base
from django.utils import timezone

from euth.contrib import base_models


def derive_mixin(request, mixin):
    model = base.ModelBase(
        '__TestModel__' + mixin.__name__,
        (mixin,),
        {'__module__': mixin.__module__})
    style = no_style()
    sql, _ = connection.creation.sql_create_model(model, style)
    cursor = connection.cursor()

    for statement in sql:
        cursor.execute(statement)

    def fin():
        sql = connection.creation.sql_destroy_model(model, (), style)
        for statement in sql:
            cursor.execute(statement)

    request.addfinalizer(fin)
    return model


@pytest.fixture
def time_stamped_model(request):
    mixin = base_models.TimeStampedModel
    return derive_mixin(request, mixin)


@pytest.mark.django_db
def test_model(time_stamped_model):
    TestModel = time_stamped_model

    with freezegun.freeze_time("2016-06-11"):
        obj = TestModel.objects.create()
        assert obj.created == timezone.now()
        created = timezone.now()
        assert obj.modified is None

    with freezegun.freeze_time("2016-06-12"):
        obj = TestModel.objects.first()
        obj.save()
        assert obj.created == created
        assert obj.modified == timezone.now()
