from adhocracy4 import emails


class ModeratorAddedEmail(emails.Email):
    template_name = 'euth_projects/emails/notify_new_moderator'

    def get_receivers(self):
        return [self.kwargs['user']]
