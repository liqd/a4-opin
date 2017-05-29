import pytest

from django.core.urlresolvers import reverse

from tests.helpers import templates_used


@pytest.mark.django_db
def test_form_view(client, organisation):
    user = organisation.initiators.first()
    client.login(username=user.email, password='password')

    url = reverse('blueprints-form', kwargs={
        'organisation_slug': organisation.slug
    })
    response = client.get(url)

    assert response.status_code == 200
    assert 'euth_blueprints/form.html' in templates_used(response)
    assert len(response.context_data['form'].errors) == 0


@pytest.mark.django_db
def test_form(client, organisation):
    user = organisation.initiators.first()
    client.login(username=user.email, password='password')

    url = reverse('blueprints-form', kwargs={
        'organisation_slug': organisation.slug
    })
    data = {
        'aim': 'collect_ideas',
        'result': '3',
        'motivation': '5',
        'experience': '4',
        'participants': '1',
        'scope': '1',
        'duration': '1',
        'accessibility': '2'
    }
    response = client.post(url, data)

    assert response.status_code == 200
    assert 'euth_blueprints/result.html' in templates_used(response)
    assert 'form' not in response.context_data
    assert len(response.context_data['blueprints']) > 0

    for b in response.context_data['blueprints']:
        # verify that for every blueprint a name, the blueprint and a
        # time is given
        assert len(b) == 3


@pytest.mark.django_db
def test_form_error(client, organisation):
    user = organisation.initiators.first()
    client.login(username=user.email, password='password')

    url = reverse('blueprints-form', kwargs={
        'organisation_slug': organisation.slug
    })
    data = {
        'aim': 'invalid',
        'result': 'invalid',
        'motivation': 'invalid',
        'experience': 'invalid',
        'participants': 'invalid',
        'scope': 'invalid',
        'duration': 'invalid',
        'accessibility': 'invalid'
    }
    response = client.post(url, data)

    assert response.status_code == 200
    assert 'euth_blueprints/form.html' in templates_used(response)
    assert len(response.context_data['form'].errors) == 8


@pytest.mark.django_db
def test_form_error_2(client, organisation):
    user = organisation.initiators.first()
    client.login(username=user.email, password='password')

    url = reverse('blueprints-form', kwargs={
        'organisation_slug': organisation.slug
    })
    data = {
        'aim': 'collect_ideas',
        'result': '3',
        'motivation': '500000',
        'experience': '4',
        'participants': '1',
        'scope': '-1',
        'duration': '1',
        'accessibility': '2'
    }
    response = client.post(url, data)

    assert response.status_code == 200
    assert 'euth_blueprints/form.html' in templates_used(response)
    assert len(response.context_data['form'].errors) == 2


@pytest.mark.django_db
def test_form_regression_fallback(client, organisation):
    user = organisation.initiators.first()
    client.login(username=user.email, password='password')

    url = reverse('blueprints-form', kwargs={
        'organisation_slug': organisation.slug
    })
    data = {
        'aim': 'collect_ideas',
        'result': '1',
        'motivation': '2',
        'experience': '1',
        'participants': '2',
        'scope': '1',
        'duration': '0',
        'accessibility': '3'
    }
    response = client.post(url, data)

    assert response.status_code == 200
    assert 'euth_blueprints/result.html' in templates_used(response)
    assert 'form' not in response.context_data
    assert len(response.context_data['blueprints']) > 0

    for b in response.context_data['blueprints']:
        # verify that for every blueprint a name, the blueprint and a
        # time is given
        assert len(b) == 3
