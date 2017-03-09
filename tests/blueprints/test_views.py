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
    }
    response = client.post(url, data)

    assert response.status_code == 200
    assert 'euth_blueprints/result.html' in templates_used(response)
