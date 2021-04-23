import pytest
from django.urls import reverse
from freezegun import freeze_time

from adhocracy4.projects.enums import Access
from euth.communitydebate import models
from euth.communitydebate import phases
from euth.communitydebate import views
from tests.helpers import redirect_target


@pytest.mark.django_db
def test_list_view(rf, phase, module_factory, topic_factory):
    module = phase.module
    project = module.project
    topic = topic_factory(module=module)
    other_module = module_factory()
    other_topic = topic_factory(module=other_module)

    with freeze_time(phase.start_date):
        view = views.TopicListView.as_view()
        request = rf.get('/topics')
        response = view(request, project=project, module=module)

        assert topic in response.context_data['topic_list']
        assert other_topic not in response.context_data['topic_list']
        assert response.context_data['topic_list'][0].comment_count == 0
        assert response.context_data['topic_list'][0].\
            positive_rating_count == 0
        assert response.context_data['topic_list'][0].\
            negative_rating_count == 0


@pytest.mark.django_db
def test_detail_view(client, topic, topic_file_upload_factory):
    url = reverse('topic-detail', kwargs={'slug': topic.slug})
    response = client.get(url)
    assert response.status_code == 200
    assert ('upload_files' in response.context_data)
    assert (response.context_data['upload_files'].count() == 0)

    topic_file = topic_file_upload_factory(topic=topic)
    assert topic_file in response.context_data['upload_files']
    topic_file.delete()


@pytest.mark.django_db
def test_detail_view_private(client, topic, user):
    topic.module.project.access = Access.PRIVATE
    topic.module.project.save()
    url = reverse('topic-detail', kwargs={'slug': topic.slug})
    response = client.get(url)
    assert response.status_code == 302
    assert redirect_target(response) == 'account_login'

    topic.module.project.participants.add(user)
    client.login(username=user.email,
                 password='password')
    response = client.get(url)
    assert response.status_code == 200

    user = topic.project.moderators.first()
    client.login(username=user.email,
                 password='password')
    response = client.get(url)
    assert response.status_code == 200

    user = topic.project.organisation.initiators.first()
    client.login(username=user.email,
                 password='password')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize('phase__type',
                         [phases.DebatePhase().identifier])
def test_create_view(client, phase, user):
    module = phase.module
    with freeze_time(phase.start_date):
        count = models.Topic.objects.all().count()
        assert count == 0
        url = reverse('topic-create', kwargs={'slug': module.slug})
        response = client.get(url)
        assert response.status_code == 302
        assert redirect_target(response) == 'account_login'
        client.login(username=user.email, password='password')
        response = client.get(url)
        assert response.status_code == 200

        upload_form_data = {'topicfileupload_set-TOTAL_FORMS': '1',
                            'topicfileupload_set-INITIAL_FORMS': '0',
                            'topicfileupload_set-MAX_NUM_FORMS': '3',
                            }
        topic = {'name': 'Topp',
                 'description': 'description'
                 }
        topic.update(upload_form_data)

        response = client.post(url, topic)
        assert response.status_code == 302
        assert redirect_target(response) == 'topic-detail'
        count = models.Topic.objects.all().count()
        assert count == 1


@pytest.mark.django_db
@pytest.mark.parametrize('phase__type',
                         [phases.DebatePhase().identifier])
def test_create_view_invalid_form(client, phase, user):
    module = phase.module
    with freeze_time(phase.start_date):
        url = reverse('topic-create', kwargs={'slug': module.slug})
        client.login(username=user.email, password='password')
        response = client.get(url)
        assert response.status_code == 200
        form_data = {'name': 'Topp',
                     'topicfileupload_set-TOTAL_FORMS': '1',
                     'topicfileupload_set-INITIAL_FORMS': '0',
                     'topicfileupload_set-MAX_NUM_FORMS': '3',
                     }
        response = client.post(url, form_data)
        assert response.status_code == 200
        assert 'This field is required'.encode() in response.content
        assert models.Topic.objects.all().count() == 0


@pytest.mark.django_db
@pytest.mark.parametrize('phase__type',
                         [phases.DebatePhase().identifier])
def test_update_view(client, phase, topic, topic_file_upload_factory):
    topic.module = phase.module
    topic.save()
    user = topic.creator
    with freeze_time(phase.start_date):
        url = reverse('topic-update', kwargs={'slug': topic.slug})
        response = client.get(url)
        assert response.status_code == 302
        client.login(username=user.email, password='password')
        response = client.get(url)
        assert response.status_code == 200
        topic_file = topic_file_upload_factory(topic=topic)
        topic_id = topic.pk
        with open(topic_file.document.path) as fp:
            upload_form_data = {'topicfileupload_set-TOTAL_FORMS': '1',
                                'topicfileupload_set-INITIAL_FORMS': '0',
                                'topicfileupload_set-MAX_NUM_FORMS': '3',
                                'topicfileupload_set-0-title':
                                    topic_file.title,
                                'topicfileupload_set-0-id': [''],
                                'topicfileupload_set-0-topic': topic_id,
                                'topicfileupload_set-0-document': fp}
            data = {'description': 'description',
                    'name': topic.name}
            data.update(upload_form_data)
            topic_file.delete()  # file is saved in post method of view
            response = client.post(url, data)
        assert response.status_code == 302
        updated_topic = models.Topic.objects.get(id=topic_id)
        assert updated_topic.description == 'description'
        assert models.TopicFileUpload.objects. \
            filter(topic=topic_id).count() == 1
        topic.delete()


@pytest.mark.django_db
@pytest.mark.parametrize('phase__type',
                         [phases.DebatePhase().identifier])
def test_delete_view_wrong_user(client, phase, topic, user, user2):
    topic.module = phase.module
    topic.creator = user
    with freeze_time(phase.start_date):
        client.login(username=user2.email, password='password')
        url = reverse('topic-delete', kwargs={'slug': topic.slug})
        response = client.post(url)
        assert response.status_code == 403
