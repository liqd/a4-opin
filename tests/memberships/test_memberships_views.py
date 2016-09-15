import pytest
from django.core import mail
from django.core.urlresolvers import reverse
from tests.helpers import redirect_target, template_used

from euth.memberships import models


@pytest.mark.django_db
def test_create_request(client, project, user):
    url = reverse('memberships-request', kwargs={'project_slug': project.slug})
    response = client.get(url)
    assert redirect_target(response) == 'account_login'

    client.login(username=user.email, password='password')
    response = client.get(url)
    assert response.status_code == 200
    assert template_used(response,
                         'euth_projects/includes/project_hero_unit.html')
    assert template_used(response, 'euth_memberships/request_detail.html')

    response = client.post(url, data={})
    assert redirect_target(response) == 'memberships-request'
    assert bool(models.Request.objects.filter(creator=user, project=project))
    assert mail.outbox[0].to == [project.moderators.first().email]


@pytest.mark.django_db
def test_accept_invite(client, invite, user):
    url = reverse('membership-invite-accept',
                  kwargs={'invite_token': invite.token})
    response = client.get(url)
    assert redirect_target(response) == 'account_login'

    client.login(username=user.email, password='password')
    response = client.get(url)
    assert response.status_code == 200
    assert template_used(response,
                         'euth_projects/includes/project_hero_unit.html')
    assert template_used(response, 'euth_memberships/invite_form.html')

    response = client.post(url, data={'accept': ''})
    assert redirect_target(response) == 'project-detail'
    assert user in invite.project.participants.all()
