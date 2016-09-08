import pytest
from django.db import IntegrityError


@pytest.mark.django_db
def test_rating_value(rating):
    assert rating.value >= -1 and rating.value <= 1


@pytest.mark.django_db
def test_rating_value_cannot_be_greater_1(rating_factory):
    rating = rating_factory(value=10)
    assert rating.value == 1


@pytest.mark.django_db
def test_rating_value_cannot_be_smaller_mius1(rating_factory):
    rating = rating_factory(value=-10)
    assert rating.value == -1


@pytest.mark.django_db
def test_rating_value_can_be_1(rating_factory):
    rating = rating_factory(value=1)
    assert rating.value == 1


@pytest.mark.django_db
def test_rating_value_can_be_0(rating_factory):
    rating = rating_factory(value=0)
    assert rating.value == 0


@pytest.mark.django_db
def test_rating_value_can_be_minus1(rating_factory):
    rating = rating_factory(value=-1)
    assert rating.value == -1


@pytest.mark.django_db
def test_user_can_rating_once(rating_factory, rating, user):

    with pytest.raises(Exception) as e:
        rating_factory(
            value=1,
            user=rating.user,
            content_type=rating.content_type,
            object_pk=rating.object_pk
        )

    assert e.type == IntegrityError
