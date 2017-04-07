import pytest

from adhocracy4.modules.models import AbstractSettings


@pytest.mark.django_db
def test_area_settings_settings(area_settings):
    module = area_settings.module
    assert isinstance(area_settings, AbstractSettings)
    assert module.settings_instance == area_settings
