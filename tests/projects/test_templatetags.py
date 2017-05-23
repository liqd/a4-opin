import pytest
from dateutil.parser import parse
from freezegun import freeze_time

from adhocracy4.test import helpers


@pytest.mark.django_db
def test_time_delta(rf, user):
    with freeze_time('2017-04-01 18:00:00 UTC'):
        request = rf.get('/')
        request.user = user
        end_date = parse('2017-04-07 18:01:00 UTC')
        template = ('{% load time_delta_tags %}'
                    '{% get_time_left end_date as time_left %}'
                    '{{ time_left|safe }}')
        context = {'request': request, 'end_date': end_date}
        helpers.render_template(template, context)

        assert '6 days and 1 minute ' == context['time_left']
