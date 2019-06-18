import pytest
from django.contrib import auth
from django.urls import reverse

User = auth.get_user_model()


@pytest.mark.django_db
def test_export_module(client, phase):
    phase.type = 'euth_ideas:collect'
    phase.save()
    user = phase.module.project.organisation.initiators.first()
    client.login(username=user.email, password='password')

    url = reverse('a4dashboard:export-module', kwargs={
        'module_slug': phase.module.slug,
        'export_id': 0,
    })
    response = client.get(url)
    assert response.status_code == 200
