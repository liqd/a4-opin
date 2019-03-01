from django.contrib.auth import get_user_model

from adhocracy4 import emails
from euth.projects import tasks

User = get_user_model()


class ModeratorAddedEmail(emails.Email):
    template_name = 'euth_projects/emails/notify_new_moderator'

    def get_receivers(self):
        return [User.objects.get(id=self.kwargs['user_id'])]


class DeleteProjectEmail(emails.Email):
    template_name = 'euth_projects/emails/delete_project'

    @classmethod
    def send_no_object(cls, object, *args, **kwargs):
        organisation = object.organisation
        object_dict = {
            'name': object.name,
            'initiators': list(organisation.initiators.all()
                               .distinct()
                               .values_list('email', flat=True)),
            'organisation': organisation.name
        }
        tasks.send_async_no_object(
            cls.__module__, cls.__name__,
            object_dict, args, kwargs)
        return []

    def get_receivers(self):
        return self.object['initiators']

    def get_context(self):
        context = super().get_context()
        context['name'] = self.object['name']
        context['organisation'] = self.object['organisation']
        return context
