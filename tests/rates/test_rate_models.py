import pytest


@pytest.mark.django_db
def test_rate_value(rate):
    assert rate.value >= -1 and rate.value <= 1


@pytest.mark.django_db
def test_rate_value_cannot_be_greater_1(rate_factory):
    rate = rate_factory(value=10)
    assert rate.value == 0


@pytest.mark.django_db
def test_rate_value_cannot_be_smaller_mius1(rate_factory):
    rate = rate_factory(value=-10)
    assert rate.value == 0


@pytest.mark.django_db
def test_rate_value_can_be_1(rate_factory):
    rate = rate_factory(value=1)
    assert rate.value == 1


@pytest.mark.django_db
def test_rate_value_can_be_0(rate_factory):
    rate = rate_factory(value=0)
    assert rate.value == 0


@pytest.mark.django_db
def test_rate_value_can_be_minus1(rate_factory):
    rate = rate_factory(value=-1)
    assert rate.value == -1
