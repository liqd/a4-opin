import pytest
from django.contrib import auth
from django.core import mail
from django.core.urlresolvers import reverse
from parler.utils.context import switch_language

from tests.helpers import redirect_target

User = auth.get_user_model()


@pytest.mark.django_db
def test_anonymous_cannot_view_dashboard_profile(client):
    url = reverse('dashboard-profile')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_authenticated_user_can_view_profile(client, user, login_url):
    url = reverse('dashboard-profile')
    client.post(login_url, {'email': user.email, 'password': 'password'})
    response = client.get(url)
    assert redirect_target(response) == 'account_login'


@pytest.mark.django_db
def test_authenticated_user_can_upload_avatar(client, user, login_url):
    url = reverse('dashboard-profile')
    client.post(login_url, {'email': user.email, 'password': 'password'})
    response = client.get(url)
    assert redirect_target(response) == 'account_login'


@pytest.mark.django_db
def test_initiator_list_projects(client, project):
    user = project.organisation.initiators.first()
    client.login(username=user.email, password='password')
    url = reverse('dashboard-project-list', kwargs={
        'organisation_slug': project.organisation.slug,
    })
    response = client.get(url)
    assert response.status_code == 200
    assert project in list(response.context_data['project_list']) == [project]


@pytest.mark.django_db
def test_initiator_create_and_update_project(client, organisation):
    user = organisation.initiators.first()
    client.login(username=user.email, password='password')
    url = reverse('dashboard-project-create', kwargs={
        'organisation_slug': organisation.slug,
        'blueprint_slug': 'brainstorming'
    })
    response = client.get(url)
    assert response.status_code == 200

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
        'phases-1-type': 'euth_ideas:020:collect',
        'phases-1-weight': '1',
        'phases-1-delete': '0',
        'project-description': 'Project description',
        'project-name': 'Project name',
        'project-information': 'Project info',
        'save_draft': ''
    })
    assert response.status_code == 302
    assert redirect_target(response) == 'dashboard-project-list'
    project = organisation.project_set.first()
    assert project.is_draft
    assert project.name == 'Project name'
    assert list(project.moderators.all()) == [user]
    assert len(project.module_set.first().phase_set.all()) == 2

    update_url = reverse('dashboard-project-edit', kwargs={
        'project_slug': project.slug
    })

    module = project.module_set.first()

    phase_1 = module.phase_set.first().pk
    phase_2 = module.phase_set.all()[1].pk

    response = client.post(update_url, {
        'phases-TOTAL_FORMS': '2',
        'phases-INITIAL_FORMS': '0',
        'phases-0-id': str(phase_1),
        'phases-0-start_date': '2016-10-01 16:12',
        'phases-0-end_date': '2016-10-01 16:13',
        'phases-0-name': 'Name 0',
        'phases-0-description': 'Description 0',
        'phases-0-type': 'euth_offlinephases:000:offline',
        'phases-0-weight': '0',
        'phases-0-delete': '1',
        'phases-1-id': str(phase_2),
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
    assert response.status_code == 302
    assert len(project.module_set.first().phase_set.all()) == 1


@pytest.mark.django_db
def test_initiator_create_flashpoll_project(client, organisation):
    user = organisation.initiators.first()
    client.login(username=user.email, password='password')
    url = reverse('dashboard-project-create', kwargs={
        'organisation_slug': organisation.slug,
        'blueprint_slug': 'flashpoll'
    })
    response = client.get(url)
    assert response.status_code == 200

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
        'project-name': 'Project name Flashpoll',
        'project-information': 'Project info',
        'save_draft': '',
        'module_settings-key': '32a34235ba14df2de',
        'module_settings-title': 'title',
        'module_settings-shortDescription': 'shortDescription',
        'module_settings-longDescription': 'longDescription',
        'module_settings-concludeMessage': 'concludeMessage',
        'module_settings-startTime': '30/01/2017 12:00',
        'module_settings-endTime': '01/02/2017 12:00',
        'module_settings-geofenceLocation': 'POLYGON' +
        '((12.721618618816137 52.71100659513395,' +
        '12.765563931316137 52.05384170239608,' +
        '14.039977993816137 52.38699960050584' +
        ',13.073181118816137 52.707678513988185' +
        ',12.721618618816137 52.71100659513395))',
    })

    assert response.status_code == 302
    assert redirect_target(response) == 'dashboard-project-list'
    project = organisation.project_set.first()
    assert project.is_draft
    assert project.name == 'Project name Flashpoll'
    assert len(project.module_set.first().phase_set.all()) == 2


@pytest.mark.django_db
def test_initiator_edit_project(client, phase):
    project = phase.module.project
    user = project.organisation.initiators.first()
    client.login(username=user.email, password='password')
    url = reverse('dashboard-project-edit', kwargs={
        'project_slug': project.slug,
    })
    response = client.get(url)
    assert response.context_data['form']['project'].instance == project
    assert response.status_code == 200


@pytest.mark.django_db
def test_project_delete(client, project):
    user = project.organisation.initiators.first()
    client.login(username=user.email, password='password')
    url = reverse('dashboard-project-delete', kwargs={
        'project_slug': project.slug
    })
    response = client.post(url, {})
    assert response.status_code == 302
    assert redirect_target(response) == 'dashboard-project-list'
    assert mail.outbox[0].to == [project.organisation.initiators.first().email]


@pytest.mark.django_db
def test_dashboard_project_users(client, project, user_factory,
                                 request_factory, invite_factory):
    url = reverse('dashboard-project-users', kwargs={
        'project_slug': project.slug,
    })
    request0 = request_factory(project=project)
    request1 = request_factory(project=project)
    request2 = request_factory(project=project)
    invite0 = invite_factory(project=project)
    invite1 = invite_factory(project=project)
    user0 = user_factory(email='test@test1.de')
    user1 = user_factory(email='test@test2.de')
    project.participants.add(user0)
    project.participants.add(user1)

    response = client.get(url)
    assert redirect_target(response) == 'account_login'

    initiator = project.organisation.initiators.first()
    client.login(username=initiator.email, password='password')
    response = client.get(url)
    assert response.status_code == 200
    multiform = response.context['form']
    assert len(multiform['requests'].forms) == 3
    assert multiform['requests'].forms[0].instance == request0
    assert multiform['requests'].forms[1].instance == request1
    assert multiform['requests'].forms[2].instance == request2
    assert multiform['requests'].extra == 0
    assert len(multiform['invites'].forms) == 2
    assert multiform['invites'].forms[0].instance == invite0
    assert multiform['invites'].forms[1].instance == invite1
    assert len(multiform['users'].forms) == 2
    assert multiform['users'].forms[0].instance == user0
    assert multiform['users'].forms[1].instance == user1

    response = client.post(url, {
        'requests-0-id': request0.pk,
        'requests-0-action': 'accept',
        'requests-1-id': request1.pk,
        'requests-1-action': 'decline',
        'requests-2-id': request2.pk,
        'requests-2-action': '',
        'requests-TOTAL_FORMS': '3',
        'requests-INITIAL_FORMS': '3',
        'requests-MAX_NUM_FORMS': '',
        'invites-TOTAL_FORMS': '2',
        'invites-INITIAL_FORMS': '2',
        'invites-MAX_NUM_FORMS': '',
        'invites-0-id': invite0.pk,
        'invites-0-delete': 'on',
        'invites-1-id': invite1.pk,
        'users-TOTAL_FORMS': '2',
        'users-INITIAL_FORMS': '2',
        'users-MAX_NUM_FORMS': '',
        'users-0-id': user0.id,
        'users-0-delete': 'on',
        'users-1-id': user1.id,
        'users-1-delete': '',
    })
    assert redirect_target(response) == 'dashboard-project-users'
    assert len(project.request_set.all()) == 1
    assert project.request_set.first() == request2
    assert len(project.invite_set.all()) == 1
    assert project.invite_set.first() == invite1
    assert len(project.participants.all()) == 2
    assert not project.participants.filter(username=user0.username).exists()
    assert User.objects.filter(username=user0.username).exists()


@pytest.mark.django_db
def test_dashboard_project_invite(client, project):
    url = reverse('dashboard-project-invite', kwargs={
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
    assert redirect_target(response) == 'dashboard-project-users'
    assert len(project.invite_set.all()) == 2
    assert project.invite_set.all()[0].email == 'j@he.ix'
    assert project.invite_set.all()[1].email == 'james.dean@gmail.com'
    assert len(mail.outbox) == 2

    response = client.post(url, {
        'emails': 'j@he.ix'
    })

    errors = response.context_data['form']['emails'].errors
    assert errors == ['j@he.ix already invited']


@pytest.mark.django_db
def test_dashboard_project_invalid(client, project):
    url = reverse('dashboard-project-invite', kwargs={
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
    url = reverse('dashboard-organisation-edit', kwargs={
        'organisation_slug': organisation.slug,
    })
    initiator = organisation.initiators.first()
    client.login(username=initiator.email, password='password')

    response = client.get(url)
    form = response.context_data['form']
    assert form.prefiled_languages() == ['en']
    assert len(form.untranslated()) == 8
    assert len(form.translated()) == 10
    assert form.translated()[0][0] == 'en'
    assert len(form.translated()[0][1]) == 4

    response = client.post(url, {
        'twitter_handle': 'a thandle',
        'place': 'Berlin',
        'country': 'DE',
        'en': 'en',
        'en__title': 'title.en',
        'en__description': 'desc.en',
        'en__description_why': 'desc why.en',
        'en__description_how': 'desc how.en',
        'de': 'de',
        'de__title': 'title.de',
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
    url = reverse('dashboard-organisation-edit', kwargs={
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
        'twitter_handle': 'a thandle',
        'place': 'Berlin',
        'country': 'DE',
        'en': 'en',
        'en__title': 'title.en',
        'en__description': 'desc.en',
        'en__description_why': 'desc why.en',
        'en__description_how': 'desc how.en',
        'de__title': 'title.de',
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


@pytest.mark.django_db
def test_dashboard_blueprint(client, organisation):
    from euth.blueprints.blueprints import blueprints
    url = reverse('dashboard-blueprint-list', kwargs={
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


@pytest.mark.django_db
def test_other_initiator_project_update(client, project, other_organisation):
    other_user = other_organisation.initiators.first()

    url = reverse('dashboard-project-edit', kwargs={
        'project_slug': project.slug
    })

    assert client.login(username=other_user.email, password='password')
    response = client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_other_initiator_project_delete(client, project, other_organisation):
    other_user = other_organisation.initiators.first()

    assert client.login(username=other_user.email, password='password')
    url = reverse('dashboard-project-delete', kwargs={
        'project_slug': project.slug
    })
    response = client.post(url, {})
    assert response.status_code == 403
    project.refresh_from_db()
    assert project.id is not None


@pytest.mark.django_db
def test_other_initiator_project_invite(client, project, other_organisation):
    other_user = other_organisation.initiators.first()

    url = reverse('dashboard-project-invite', kwargs={
        'project_slug': project.slug,
    })

    assert client.login(username=other_user.email, password='password')
    response = client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_initiator_archive_project(client, organisation):
    user = organisation.initiators.first()
    client.login(username=user.email, password='password')
    url = reverse('dashboard-project-create', kwargs={
        'organisation_slug': organisation.slug,
        'blueprint_slug': 'brainstorming'
    })
    response = client.get(url)
    assert response.status_code == 200

    # Archiving a not yet created project must fail. The
    # project is created but not archived.
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
        'phases-1-type': 'euth_ideas:020:collect',
        'phases-1-weight': '1',
        'phases-1-delete': '0',
        'project-description': 'Project description',
        'project-name': 'Project name',
        'project-information': 'Project info',
        'archive': ''
    })
    assert response.status_code == 302
    assert redirect_target(response) == 'dashboard-project-list'
    project = organisation.project_set.first()
    assert not project.is_archived
    assert project.name == 'Project name'
    assert list(project.moderators.all()) == [user]
    assert len(project.module_set.first().phase_set.all()) == 2

    update_url = reverse('dashboard-project-edit', kwargs={
        'project_slug': project.slug
    })

    module = project.module_set.first()

    phase_1 = module.phase_set.first().pk
    phase_2 = module.phase_set.all()[1].pk

    # Archiving a project that has running phases must fail.
    response = client.post(update_url, {
        'phases-TOTAL_FORMS': '2',
        'phases-INITIAL_FORMS': '0',
        'phases-0-id': str(phase_1),
        'phases-0-start_date': '2016-10-01 16:12',
        'phases-0-end_date': '2016-10-01 16:13',
        'phases-0-name': 'Name 0',
        'phases-0-description': 'Description 0',
        'phases-0-type': 'euth_offlinephases:000:offline',
        'phases-0-weight': '0',
        'phases-0-delete': '1',
        'phases-1-id': str(phase_2),
        'phases-1-start_date': '2016-10-01 16:14',
        'phases-1-end_date': '2099-10-01 16:15',
        'phases-1-name': 'Name 1',
        'phases-1-description': 'Description 1',
        'phases-1-type': 'euth_maps:020:collect',
        'phases-1-weight': '1',
        'phases-1-delete': '0',
        'project-description': 'Project description',
        'project-name': 'Project name',
        'project-information': 'Project info',
        'archive': ''
    })
    project = organisation.project_set.first()
    assert response.status_code == 302
    assert not project.is_archived
    assert len(project.module_set.first().phase_set.all()) == 1


@pytest.mark.django_db
def test_initiator_archive_project_success(client, organisation):
    user = organisation.initiators.first()
    client.login(username=user.email, password='password')
    url = reverse('dashboard-project-create', kwargs={
        'organisation_slug': organisation.slug,
        'blueprint_slug': 'brainstorming'
    })
    response = client.get(url)
    assert response.status_code == 200

    # Archiving a not yet created project must fail. The
    # project is created but not archived.
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
        'phases-1-type': 'euth_ideas:020:collect',
        'phases-1-weight': '1',
        'phases-1-delete': '0',
        'project-description': 'Project description',
        'project-name': 'Project name',
        'project-information': 'Project info',
    })
    assert response.status_code == 302
    assert redirect_target(response) == 'dashboard-project-list'
    project = organisation.project_set.first()
    assert project.name == 'Project name'
    assert list(project.moderators.all()) == [user]
    assert len(project.module_set.first().phase_set.all()) == 2

    update_url = reverse('dashboard-project-edit', kwargs={
        'project_slug': project.slug
    })

    module = project.module_set.first()

    phase_1 = module.phase_set.first().pk
    phase_2 = module.phase_set.all()[1].pk

    # Archiving a project without any running phase
    # must succeed
    response = client.post(update_url, {
        'phases-TOTAL_FORMS': '2',
        'phases-INITIAL_FORMS': '0',
        'phases-0-id': str(phase_1),
        'phases-0-start_date': '2016-10-01 16:12',
        'phases-0-end_date': '2016-10-01 16:13',
        'phases-0-name': 'Name 0',
        'phases-0-description': 'Description 0',
        'phases-0-type': 'euth_offlinephases:000:offline',
        'phases-0-weight': '0',
        'phases-0-delete': '1',
        'phases-1-id': str(phase_2),
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
        'archive': ''
    })
    project = organisation.project_set.first()
    assert response.status_code == 302
    assert project.is_archived
    assert len(project.module_set.first().phase_set.all()) == 1


@pytest.mark.django_db
def test_initiator_archive_project_broken(client, organisation):
    user = organisation.initiators.first()
    client.login(username=user.email, password='password')
    url = reverse('dashboard-project-create', kwargs={
        'organisation_slug': organisation.slug,
        'blueprint_slug': 'brainstorming'
    })
    response = client.get(url)
    assert response.status_code == 200

    # Archiving a not yet created project must fail. The
    # project is created but not archived.
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
        'phases-1-type': 'euth_ideas:020:collect',
        'phases-1-weight': '1',
        'phases-1-delete': '0',
        'project-description': 'Project description',
        'project-name': 'Project name',
        'project-information': 'Project info',
        'archive': ''
    })
    assert response.status_code == 302
    assert redirect_target(response) == 'dashboard-project-list'
    project = organisation.project_set.first()
    assert not project.is_archived
    assert project.name == 'Project name'
    assert list(project.moderators.all()) == [user]
    assert len(project.module_set.first().phase_set.all()) == 2

    update_url = reverse('dashboard-project-edit', kwargs={
        'project_slug': project.slug
    })

    module = project.module_set.first()

    phase_1 = module.phase_set.first().pk
    phase_2 = module.phase_set.all()[1].pk

    # Archiving a project with endless phase is archivable
    response = client.post(update_url, {
        'phases-TOTAL_FORMS': '2',
        'phases-INITIAL_FORMS': '0',
        'phases-0-id': str(phase_1),
        'phases-0-start_date': '2016-10-01 16:12',
        'phases-0-end_date': '2016-10-01 16:13',
        'phases-0-name': 'Name 0',
        'phases-0-description': 'Description 0',
        'phases-0-type': 'euth_offlinephases:000:offline',
        'phases-0-weight': '0',
        'phases-0-delete': '1',
        'phases-1-id': str(phase_2),
        'phases-1-start_date': '2016-10-01 16:14',
        'phases-1-name': 'Name 1',
        'phases-1-description': 'Description 1',
        'phases-1-type': 'euth_maps:020:collect',
        'phases-1-weight': '1',
        'phases-1-delete': '0',
        'project-description': 'Project description',
        'project-name': 'Project name',
        'project-information': 'Project info',
        'archive': ''
    })
    project = organisation.project_set.first()
    assert response.status_code == 302
    assert project.is_archived
    assert len(project.module_set.first().phase_set.all()) == 1
