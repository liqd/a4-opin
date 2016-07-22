import pytest

from ..apps.blog import models


@pytest.fixture
def time_stamped_model():
    return models.Post
