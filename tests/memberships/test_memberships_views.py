import pytest
from django.core import mail
from django.core.urlresolvers import reverse

from euth.memberships import models
from tests.helpers import redirect_target, templates_used
from tests.memberships.factories import InviteFactory


@pytest.mark.django_db
@pytest.mark.parametrize('project__is_public', [False])
def test_detail_private_project(client, project, user):
    project_url = reverse('project-detail', args=[project.slug])
    response = client.get(project_url)
    assert response.status_code == 302
    assert redirect_target(response) == 'account_login'

    client.login(username=user.email, password='password')
    response = client.get(project_url)
    assert response.status_code == 302
    assert redirect_target(response) == 'memberships-request'

    project.participants.add(user)
    response = client.get(project_url)
    assert response.status_code == 200
    assert response.context_data['view'].project == project


@pytest.mark.django_db
@pytest.mark.parametrize('project__is_draft', [True])
def test_detail_draft_project(client, project, user):
    project_url = reverse('project-detail', args=[project.slug])
    response = client.get(project_url)
    assert response.status_code == 302
    assert redirect_target(response) == 'account_login'

    client.login(username=user.email, password='password')
    response = client.get(project_url)
    assert response.status_code == 403
    assert (
        'euth_projects/project_membership_request.html'
        not in templates_used(response)
    )

    project.participants.add(user)
    response = client.get(project_url)
    assert response.status_code == 403
    assert (
        'euth_projects/project_membership_request.html'
        not in templates_used(response)
    )

    project.organisation.initiators.add(user)
    response = client.get(project_url)
    assert response.status_code == 200
    assert response.context_data['view'].project == project


@pytest.mark.parametrize('project__is_public', [False])
@pytest.mark.django_db
def test_create_request(client, project, user):
    url = reverse('memberships-request', kwargs={'project_slug': project.slug})
    response = client.get(url)
    assert redirect_target(response) == 'account_login'

    client.login(username=user.email, password='password')
    response = client.get(url)
    assert response.status_code == 200
    assert (
        'euth_projects/includes/project_hero_unit.html'
        in templates_used(response)
    )
    assert 'euth_memberships/request_detail.html' in templates_used(response)

    response = client.post(url, data={})
    assert redirect_target(response) == 'memberships-request'
    assert bool(models.Request.objects.filter(creator=user, project=project))
    assert mail.outbox[0].to == [project.moderators.first().email]

    project.participants.add(user)
    response = client.get(url)
    assert redirect_target(response) == 'project-detail'


@pytest.mark.django_db
def test_cant_accept_invite(client, invite, user):
    url = reverse('membership-invite-accept',
                  kwargs={'invite_token': invite.token})
    response = client.get(url)
    assert redirect_target(response) == 'account_login'

    client.login(username=user.email, password='password')
    response = client.get(url)
    assert response.status_code == 200
    assert (
        'euth_projects/includes/project_hero_unit.html'
        in templates_used(response)
    )
    assert 'euth_memberships/invite_form.html' in templates_used(response)

    response = client.post(url, data={'accept': ''})
    assert response.status_code == 200
    assert (
        'This user has another email address '
        'than the one that received the invitation.'
        in response.context['form'].errors['__all__']
    )
    assert user not in invite.project.participants.all()


@pytest.mark.django_db
def test_accept_invite(client, user):
    invite = InviteFactory(email=user.email)
    assert invite.email == user.email
    url = reverse('membership-invite-accept',
                  kwargs={'invite_token': invite.token})
    response = client.get(url)
    assert redirect_target(response) == 'account_login'

    client.login(username=user.email, password='password')
    response = client.get(url)
    assert response.status_code == 200
    assert (
        'euth_projects/includes/project_hero_unit.html'
        in templates_used(response)
    )
    assert 'euth_memberships/invite_form.html' in templates_used(response)

    response = client.post(url, data={'accept': ''})
    assert redirect_target(response) == 'project-detail'
    assert user in invite.project.participants.all()
