import pytest


@pytest.mark.django_db
def test_str(flashpoll):
    fp_string = str(flashpoll)
    assert fp_string == flashpoll.key


@pytest.mark.django_db
def test_flashpoll_settgins(flashpoll):
    module = flashpoll.module
    assert module.settings_instance == flashpoll
