import pytest
from django.core import exceptions

from euth.phases import validators


def test_validator_with_testapp():
    assert validators.validate_content('blog:020:phase') == 'blog:020:phase'


def test_validator_invalid_phase():
    with pytest.raises(exceptions.ValidationError):
        validators.validate_content('noapp:020:nophase')
