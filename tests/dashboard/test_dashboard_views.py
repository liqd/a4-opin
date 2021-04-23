import pytest
from django.contrib import auth
from django.core import mail
from django.urls import reverse
from parler.utils.context import switch_language

from adhocracy4.projects.enums import Access
from adhocracy4.projects.models import Project
from tests.helpers import redirect_target

User = auth.get_user_model()


@pytest.fixture()
@pytest.mark.django_db
def new_project(organisation, client):
    user = organisation.initiators.first()
    client.login(username=user.email, password='password')
    url = reverse('a4dashboard:project-create', kwargs={
        'organisation_slug': organisation.slug,
        'blueprint_slug': 'brainstorming'
    })
    response = client.get(url)
    assert response.status_code == 200

    # Create project
    response = client.post(url, {
        'description': 'Project description',
        'name': 'Project name'
    })
    assert response.status_code == 302
    assert redirect_target(response) == 'project-create'
    project = organisation.project_set.first()
    assert not project.is_archived
    assert project.name == 'Project name'
    return project


@pytest.mark.django_db
def test_initiator_list_projects(client, project):
    user = project.organisation.initiators.first()
    client.login(username=user.email, password='password')
    url = reverse('a4dashboard:project-list', kwargs={
        'organisation_slug': project.organisation.slug,
    })
    response = client.get(url)
    assert response.status_code == 200
    assert project in list(response.context_data['project_list']) == [project]


@pytest.mark.django_db
def test_initiator_create_project(client, organisation):
    user = organisation.initiators.first()
    client.login(username=user.email, password='password')
    url = reverse('a4dashboard:project-create', kwargs={
        'organisation_slug': organisation.slug,
        'blueprint_slug': 'brainstorming'
    })
    response = client.get(url)
    assert response.status_code == 200

    response = client.post(url, {
        'name': 'Project name',
        'description': 'Project info'
    })
    assert response.status_code == 302
    assert redirect_target(response) == 'project-edit'
    project = organisation.project_set.first()
    assert project.is_draft
    assert project.name == 'Project name'


@pytest.mark.django_db
def test_initiator_edit_project(client, phase):
    project = phase.module.project
    user = project.organisation.initiators.first()
    client.login(username=user.email, password='password')
    url = reverse('a4dashboard:dashboard-basic-edit', kwargs={
        'project_slug': project.slug,
    })
    response = client.get(url)
    assert response.context_data['form'].instance == project
    assert response.status_code == 200

    client.post(url, {
        'name': 'Project name',
        'description': 'Project info',
        'access': Access.PUBLIC.value
    })

    project = Project.objects.get(id=project.id)
    assert project.name == 'Project name'
    assert project.description == 'Project info'


@pytest.mark.django_db
def test_dashboard_project_moderators(client, project, user_factory):
    url = reverse('a4dashboard:moderators', kwargs={
        'project_slug': project.slug,
    })

    response = client.get(url)
    assert redirect_target(response) == 'account_login'

    initiator = project.organisation.initiators.first()
    client.login(username=initiator.email, password='password')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_dashboard_project_members_requests(client, project,
                                            request_factory):
    url = reverse('a4dashboard:members', kwargs={
        'project_slug': project.slug,
    })
    request0 = request_factory(project=project)
    request1 = request_factory(project=project)
    request2 = request_factory(project=project)

    response = client.get(url)
    assert redirect_target(response) == 'account_login'

    initiator = project.organisation.initiators.first()
    client.login(username=initiator.email, password='password')
    response = client.get(url)
    assert response.status_code == 200

    response = client.post(url, {
        'form-TOTAL_FORMS': '3',
        'form-INITIAL_FORMS': '3',
        'form-MIN_NUM_FORMS': '0',
        'form-MAX_NUM_FORMS': '1000',
        'form-0-id': request0.id,
        'form-0-action': 'accept',
        'form-1-id': request1.id,
        'form-1-action': 'accept',
        'form-2-id': request2.id,
        'form-2-action': 'decline',
        'submit_action': 'update_request'
    })

    assert redirect_target(response) == 'members'
    assert len(project.request_set.all()) == 0
    assert len(project.participants.all()) == 2


@pytest.mark.django_db
def test_dashboard_project_members_delete(client, project, user_factory):
    url = reverse('a4dashboard:members', kwargs={
        'project_slug': project.slug,
    })
    user0 = user_factory(email='test@test1.de')
    user1 = user_factory(email='test@test2.de')
    project.participants.add(user0)
    project.participants.add(user1)

    assert len(project.participants.all()) == 2

    response = client.get(url)
    assert redirect_target(response) == 'account_login'

    initiator = project.organisation.initiators.first()
    client.login(username=initiator.email, password='password')
    response = client.get(url)
    assert response.status_code == 200

    response = client.post(url, {
        'form-TOTAL_FORMS': '2',
        'form-INITIAL_FORMS': '2',
        'form-MIN_NUM_FORMS': '0',
        'form-MAX_NUM_FORMS': '1000',
        'form-0-id': user0.id,
        'form-0-delete': 'on',
        'form-1-id': user1.id,
        'submit_action': 'remove_members'
    })

    assert redirect_target(response) == 'members'
    assert len(project.participants.all()) == 1


@pytest.mark.django_db
def test_dashboard_project_invite(client, project):
    url = reverse('a4dashboard:invites', kwargs={
        'project_slug': project.slug,
    })

    response = client.get(url)
    assert redirect_target(response) == 'account_login'

    initiator = project.organisation.initiators.first()
    client.login(username=initiator.email, password='password')
    response = client.get(url)
    assert response.status_code == 200

    response = client.post(url, {
        'emails': 'j@he.ix, james.dean@gmail.com'
    })

    assert redirect_target(response) == 'invites'
    assert len(project.invite_set.all()) == 2
    # assert project.invite_set.all()[0].email == 'j@he.ix'
    # assert project.invite_set.all()[1].email == 'james.dean@gmail.com'
    assert len(mail.outbox) == 2

    response = client.post(url, {
        'emails': 'j@he.ix'
    })

    errors = response.context_data['form']['emails'].errors
    assert errors == ['j@he.ix already invited']


@pytest.mark.django_db
def test_dashboard_project_invalid(client, project):
    url = reverse('a4dashboard:invites', kwargs={
        'project_slug': project.slug,
    })

    initiator = project.organisation.initiators.first()
    client.login(username=initiator.email, password='password')

    response = client.post(url, {
        'emails': 'test@test.de foo@bar.de'
    })
    errors = response.context_data['form']['emails'].errors
    assert errors == ['Please enter correct e-mail addresses,'
                      ' separated by commas.']

    response = client.post(url, {
        'emails': 'test@foo, @aded'
    })
    errors = response.context_data['form']['emails'].errors
    assert errors == ['Please enter correct e-mail addresses,'
                      ' separated by commas.']


@pytest.mark.django_db
def test_dashboard_update_organisation(client, organisation):
    url = reverse('a4dashboard:organisation-edit', kwargs={
        'organisation_slug': organisation.slug,
    })
    initiator = organisation.initiators.first()
    client.login(username=initiator.email, password='password')

    response = client.get(url)
    form = response.context_data['form']
    assert form.prefilled_languages() == ['en']
    assert len(form.untranslated()) == 9
    assert len(form.translated()) == 10
    assert form.translated()[0][0] == 'en'
    assert len(form.translated()[0][1]) == 3

    response = client.post(url, {
        'name': 'name.de',
        'twitter_handle': 'a thandle',
        'place': 'Berlin',
        'country': 'DE',
        'en': 'en',
        'en__description': 'desc.en',
        'en__description_why': 'desc why.en',
        'en__description_how': 'desc how.en',
        'de': 'de',
        'de__description': 'desc.de',
        'de__description_why': 'desc why.de',
        'de__description_how': 'desc how.de',
    })
    response.status_code == 200

    organisation.refresh_from_db()
    organisation.get_translation('en').refresh_from_db()
    assert organisation.place == 'Berlin'
    assert organisation.twitter_handle == 'a thandle'
    assert organisation.description == 'desc.en'

    with switch_language(organisation, 'de'):
        assert organisation.description == 'desc.de'


@pytest.mark.django_db
def test_dashboard_organisation_delete_language(client, organisation):
    url = reverse('a4dashboard:organisation-edit', kwargs={
        'organisation_slug': organisation.slug,
    })

    initiator = organisation.initiators.first()
    client.login(username=initiator.email, password='password')

    with switch_language(organisation, 'de'):
        organisation.description = 'desc.de'
        organisation.description_why = 'desc why.de'
        organisation.description_how = 'desc how.de'
        organisation.save()

    response = client.post(url, {
        'name': 'name.en',
        'twitter_handle': 'a thandle',
        'place': 'Berlin',
        'country': 'DE',
        'en': 'en',
        'en__description': 'desc.en',
        'en__description_why': 'desc why.en',
        'en__description_how': 'desc how.en',
        'de__description': 'desc.de',
        'de__description_why': 'desc why.de',
        'de__description_how': 'desc how.de',
    })
    response.status_code == 200

    organisation.refresh_from_db()
    organisation.get_translation('en').refresh_from_db()
    with switch_language(organisation, 'de'):
        organisation.description = 'desc.en'
        organisation.description_why = 'desc why.en'
        organisation.description_how = 'desc how.en'
        organisation.save()


'''
@pytest.mark.django_db
def test_dashboard_blueprint(client, organisation):
    from euth.blueprints.blueprints import blueprints
    url = reverse('a4dashboard:blueprint-list', kwargs={
        'organisation_slug': organisation.slug
    })
    user = organisation.initiators.first()
    response = client.get(url)
    assert response.status_code == 302
    assert redirect_target(response) == 'account_login'
    client.login(username=user.email, password='password')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context_data['view'].blueprints == blueprints
'''


@pytest.mark.django_db
def test_other_initiator_project_update(client, project, other_organisation):
    other_user = other_organisation.initiators.first()

    url = reverse('a4dashboard:dashboard-basic-edit', kwargs={
        'project_slug': project.slug
    })

    assert client.login(username=other_user.email, password='password')
    response = client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_other_initiator_project_invite(client, project, other_organisation):
    other_user = other_organisation.initiators.first()

    url = reverse('a4dashboard:members', kwargs={
        'project_slug': project.slug,
    })

    assert client.login(username=other_user.email, password='password')
    response = client.get(url)
    assert response.status_code == 403
