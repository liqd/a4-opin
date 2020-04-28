import pytest

from adhocracy4.test import helpers


@pytest.mark.django_db
def test_get_range(rf):
    request = rf.get('/')
    template = ('{% load idea_tags %}'
                '{% get_range page_number_1 page_num_pages as range_1 %}'
                '{% get_range page_number_5 page_num_pages as range_5 %}'
                '{% get_range page_number_11 page_num_pages as range_11 %}'
                '{{ range_1 }}'
                '{{ range_5 }}'
                '{{ range_11 }}')
    context = {'request': request,
               'page_number_1': 1,
               'page_number_5': 5,
               'page_number_11': 11,
               'page_num_pages': 12}
    helpers.render_template(template, context)

    assert range(1, 6) == context['range_1']
    assert range(3, 8) == context['range_5']
    assert range(8, 13) == context['range_11']


@pytest.mark.django_db
def test_combined_url_parameter(rf):
    request = rf.get('/?bla=bums&da=dings')
    template = ('{% load idea_tags %}'
                '{% combined_url_parameter request.GET as url_par_1 %}'
                '{% combined_url_parameter request.GET bla="" as url_par_2 %}'
                '{{ url_par_1 }}'
                '{{ url_par_2 }}')
    context = {'request': request}
    helpers.render_template(template, context)

    assert 'bla=bums' in context['url_par_1']
    assert 'da=dings' in context['url_par_1']
    assert 'bla=' in context['url_par_2']
    assert 'da=dings' in context['url_par_2']
