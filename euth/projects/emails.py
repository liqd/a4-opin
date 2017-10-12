from django.contrib.auth import get_user_model

from adhocracy4 import emails

User = get_user_model()


class ModeratorAddedEmail(emails.Email):
    template_name = 'euth_projects/emails/notify_new_moderator'

    def get_receivers(self):
        return [User.objects.get(id=self.kwargs['user_id'])]
