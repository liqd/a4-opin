import pytest

from euth.follows import models


@pytest.mark.django_db
def test_autofollow_hook(user, idea_factory):

    idea = idea_factory(creator=user)
    follow = models.Follow.objects.get(creator=user, project=idea.project)
    assert follow
    assert follow.enabled

    follow.enabled = False
    follow.save()

    idea = idea_factory(creator=user, module=idea.module)
    follow = models.Follow.objects.get(creator=user, project=idea.project)
    assert follow
    assert not follow.enabled
