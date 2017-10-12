import pytest
from django.core.urlresolvers import reverse
from django.utils import timezone
from freezegun import freeze_time

from euth.ideas import models, phases, views
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
@pytest.mark.parametrized('idea__module__project__is_public',
                          [False])
def test_detail_view_private(client, idea, user):
    idea.module.project.is_public = False
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


@pytest.mark.django_db
def test_sort_mixin(rf):
    from tests.apps.blog.models import Post
    from django.views import generic

    post1 = Post(heading="B", body="text A")
    post1.save()
    post2 = Post(heading="A", body="text A")
    post2.save()

    class FakeSortView(views.SortMixin, generic.ListView):
        model = Post
        sort_default = 'heading'
        sorts = [
            ('heading', 'sort by heading'),
            ('created', 'sort by created')
        ]
    view = FakeSortView.as_view()

    response = view(rf.get('/'))
    assert response.context_data['view'].sort == 'heading'
    assert list(response.context_data['post_list']) == [post2, post1]

    response = view(rf.get('/', {'sort': 'invalid'}))
    assert response.context_data['view'].sort == 'heading'
    assert list(response.context_data['post_list']) == [post2, post1]

    response = view(rf.get('/', {'sort': 'created'}))
    assert response.context_data['view'].sort == 'created'
    assert list(response.context_data['post_list']) == [post1, post2]


@pytest.mark.django_db
def test_ideas_download_by_anonymous_forbidden(client, idea_factory, user):

    idea = idea_factory()
    module = idea.module
    url = reverse('idea-download', kwargs={'slug': module.slug})
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_ideas_download_by_authenticated_user_forbidden(
        client, idea_factory, user):
    idea1 = idea_factory()
    module = idea1.module
    url = reverse('idea-download', kwargs={'slug': module.slug})
    client.login(username=user.email, password='password')
    response = client.get(url)
    assert response.status_code == 403
    module.project.moderators.add(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_ideas_download_by_moderator_is_allowed(client, idea_factory, user):
    idea1 = idea_factory()
    module = idea1.module
    url = reverse('idea-download', kwargs={'slug': module.slug})
    client.login(username=user.email, password='password')
    module.project.moderators.add(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_ideas_download_by_initiator_is_allowed(client, idea_factory, user):
    idea1 = idea_factory()
    module = idea1.module
    url = reverse('idea-download', kwargs={'slug': module.slug})
    client.login(username=user.email, password='password')
    module.project.organisation.initiators.add(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_ideas_download_by_admin_is_allowed(client, idea_factory, admin):
    idea1 = idea_factory()
    module = idea1.module
    url = reverse('idea-download', kwargs={'slug': module.slug})
    client.login(username=admin.email, password='password')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_ideas_download_contains_right_data(rf, idea_factory, admin):
    idea = idea_factory()
    module = idea.module
    idea_factory(module=module)
    idea_factory(module=module)

    now = timezone.now()
    with freeze_time(now):
        request = rf.get('/ideas/download/module/{}'.format(module.slug))
        request.user = admin
        response = views.IdeaDownloadView.as_view()(request, slug=module.slug)
        assert response.status_code == 200
        assert (response._headers['content-type'] ==
                ('Content-Type',
                'application/vnd.openxmlformats-officedocument'
                    '.spreadsheetml.sheet'))
        assert (response._headers['content-disposition'] ==
                ('Content-Disposition',
                 'attachment; filename="{}_{}.xlsx"'
                 .format(
                     module.project.slug,
                     now.strftime('%Y%m%dT%H%M%S'))))
