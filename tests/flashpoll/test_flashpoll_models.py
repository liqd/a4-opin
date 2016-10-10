import pytest


@pytest.mark.django_db
def test_str(flashpoll):
    idea_string = flashpoll.__str__()
    assert idea_string == flashpoll.key


@pytest.mark.django_db
def test_project(flashpoll):
    assert flashpoll.module.project == flashpoll.project
