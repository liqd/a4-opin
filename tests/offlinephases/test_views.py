import pytest
from django.core.urlresolvers import reverse

from euth.offlinephases import models as offlinephase_models


@pytest.mark.django_db
def test_initiator_can_edit_offlinephase(client, organisation):
    user = organisation.initiators.first()
    client.login(username=user.email, password='password')
    url = reverse('dashboard-project-create', kwargs={
        'organisation_slug': organisation.slug,
        'blueprint_slug': 'ideas-collection-1'
    })
    response = client.get(url)

    response = client.post(url, {
        'phases-TOTAL_FORMS': '2',
        'phases-INITIAL_FORMS': '0',
        'phases-0-id': '',
        'phases-0-start_date': '2016-10-01 16:12',
        'phases-0-end_date': '2016-10-01 16:13',
        'phases-0-name': 'Name 0',
        'phases-0-description': 'Description 0',
        'phases-0-type': 'euth_offlinephases:000:offline',
        'phases-0-weight': '0',
        'phases-0-delete': '0',
        'phases-1-id': '',
        'phases-1-start_date': '2016-10-01 16:14',
        'phases-1-end_date': '2016-10-01 16:15',
        'phases-1-name': 'Name 1',
        'phases-1-description': 'Description 1',
        'phases-1-type': 'euth_maps:020:collect',
        'phases-1-weight': '1',
        'phases-1-delete': '0',
        'project-description': 'Project description',
        'project-name': 'Project name',
        'project-information': 'Project info',
        'save_draft': ''
    })

    project = organisation.project_set.first()
    assert project.module_set.first().phase_set.count() == 2
    offlinephase = project.module_set.first().phase_set.first()
    assert offlinephase.type == 'euth_offlinephases:000:offline'
    assert offlinephase_models.Offlinephase.objects.filter(
        phase=offlinephase).exists()
    assert offlinephase_models.Offlinephase.objects.filter(
        phase=offlinephase).count() == 1
    op_documentation = offlinephase.offlinephase

    url = reverse('offlinephase-edit', kwargs={'pk': op_documentation.pk})
    response = client.get(url)
    assert response.status_code == 200

    response = client.post(url, {
        'fileuploads-TOTAL_FORMS': '1',
        'fileuploads-INITIAL_FORMS': '0',
        'fileuploads-MIN_NUM_FORMS': '0',
        'fileuploads-MAX_NUM_FORMS': '5',
        'offlinephase-text': 'Lorem ipsum'
    })

    assert response.status_code == 302
