import pytest
from django.urls import reverse
from freezegun import freeze_time

from adhocracy4.projects.enums import Access
from euth.ideas import models
from euth.ideas import phases
from euth.ideas import views
from tests.helpers import redirect_target


@pytest.mark.django_db
def test_list_view(rf, phase, module_factory, idea_factory):
    module = phase.module
    project = module.project
    idea = idea_factory(module=module)
    other_module = module_factory()
    other_idea = idea_factory(module=other_module)

    with freeze_time(phase.start_date):
        view = views.IdeaListView.as_view()
        request = rf.get('/ideas')
        response = view(request, project=project, module=module)

        assert idea in response.context_data['idea_list']
        assert other_idea not in response.context_data['idea_list']
        assert response.context_data['idea_list'][0].comment_count == 0
        assert response.context_data['idea_list'][0].positive_rating_count == 0
        assert response.context_data['idea_list'][0].negative_rating_count == 0


@pytest.mark.django_db
def test_detail_view(client, phase, idea):
    url = reverse('idea-detail', kwargs={'slug': idea.slug})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_detail_view_private(client, idea, user):
    idea.module.project.access = Access.PRIVATE
    idea.module.project.save()
    url = reverse('idea-detail', kwargs={'slug': idea.slug})
    response = client.get(url)
    assert response.status_code == 302
    assert redirect_target(response) == 'account_login'

    idea.module.project.participants.add(user)
    client.login(username=user.email,
                 password='password')
    response = client.get(url)
    assert response.status_code == 200

    user = idea.project.moderators.first()
    client.login(username=user.email,
                 password='password')
    response = client.get(url)
    assert response.status_code == 200

    user = idea.project.organisation.initiators.first()
    client.login(username=user.email,
                 password='password')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize('phase__type',
                         [phases.CollectPhase().identifier])
def test_create_view(client, phase, user):
    module = phase.module
    with freeze_time(phase.start_date):
        count = models.Idea.objects.all().count()
        assert count == 0
        url = reverse('idea-create', kwargs={'slug': module.slug})
        response = client.get(url)
        assert response.status_code == 302
        assert redirect_target(response) == 'account_login'
        client.login(username=user.email, password='password')
        response = client.get(url)
        assert response.status_code == 200
        idea = {'name': 'Idea', 'description': 'description'}
        response = client.post(url, idea)
        assert response.status_code == 302
        assert redirect_target(response) == 'idea-detail'
        count = models.Idea.objects.all().count()
        assert count == 1


@pytest.mark.django_db
@pytest.mark.parametrize('phase__type',
                         [phases.RatingPhase().identifier])
def test_create_view_wrong_phase(client, phase, user):
    module = phase.module
    with freeze_time(phase.start_date):
        url = reverse('idea-create', kwargs={'slug': module.slug})
        response = client.get(url)
        assert response.status_code == 302
        client.login(username=user.email, password='password')
        response = client.get(url)
        assert response.status_code == 403


@pytest.mark.django_db
@pytest.mark.parametrize('phase__type',
                         [phases.CollectPhase().identifier])
def test_update_view(client, phase, idea):
    idea.module = phase.module
    idea.save()
    user = idea.creator
    with freeze_time(phase.start_date):
        url = reverse('idea-update', kwargs={'slug': idea.slug})
        response = client.get(url)
        assert response.status_code == 302
        client.login(username=user.email, password='password')
        response = client.get(url)
        assert response.status_code == 200
        data = {'description': 'description', 'name': idea.name}
        response = client.post(url, data)
        id = idea.pk
        updated_idea = models.Idea.objects.get(id=id)
        assert updated_idea.description == 'description'
        assert response.status_code == 302


@pytest.mark.django_db
@pytest.mark.parametrize('phase__type',
                         [phases.CollectPhase().identifier])
def test_delete_view_wrong_user(client, phase, idea, user, user2):
    idea.module = phase.module
    idea.creator = user
    with freeze_time(phase.start_date):
        client.login(username=user2.email, password='password')
        url = reverse('idea-delete', kwargs={'slug': idea.slug})
        response = client.post(url)
        assert response.status_code == 403
