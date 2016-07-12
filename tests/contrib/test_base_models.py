from django.db import connection, models
from django.db.models import base
from django.core.management.color import no_style
from django.utils import timezone

import freezegun
import pytest

from euth.contrib import base_models

@pytest.fixture
def time_stamped_model(request, db):
    mixin = base_models.TimeStampedModel
    model = base.ModelBase(
        '__TestModel__' + mixin.__name__,
        (mixin,),
        { '__module__': mixin.__module__ })
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

def test_model(time_stamped_model):
    TestModel = time_stamped_model

    with freezegun.freeze_time("2016-06-11"):
        obj = TestModel.objects.create()
        assert obj.created == timezone.now()
        created = timezone.now()
        assert obj.modified == None

    with freezegun.freeze_time("2016-06-12"):
        obj = TestModel.objects.first()
        obj.save()
        assert obj.created == created
        assert obj.modified == timezone.now()
