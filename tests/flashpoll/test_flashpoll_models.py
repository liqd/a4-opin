import pytest

from euth.modules.models import AbstractSettings


@pytest.mark.django_db
def test_str(flashpoll):
    idea_string = flashpoll.__str__()
    assert idea_string == flashpoll.key


@pytest.mark.django_db
def test_flashpoll_settgins(flashpoll):
    module = flashpoll.module
    assert isinstance(flashpoll, AbstractSettings)
    assert module.settings_instance == flashpoll
