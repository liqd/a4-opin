import pytest

from euth.modules.models import AbstractSettings


@pytest.mark.django_db
def test_area_settings_settings(area_settings):
    module = area_settings.module
    assert isinstance(area_settings, AbstractSettings)
    assert module.settings_instance == area_settings

'''
@pytest.mark.django_db
def test_empty_features_validation(area_settings):
    empty_geojson = json.dumps({
        "type": "FeatureCollection",
        "features": []
    })
    with pytest.raises(Exception) as e:
        area_settings.polygon = empty_geojson
        area_settings.full_clean()
    assert 'Field can not be empty' in str(e)
'''
