import pytest
from django.core.urlresolvers import reverse


@pytest.mark.django_db
def test_list_view(client, project):
    url = reverse('project-list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_detail_view(client, project):
    project_url = reverse('project-detail', args=[project.slug])
    response = client.get(project_url)
    assert response.status_code == 200
    assert response.context_data['view'].project == project
