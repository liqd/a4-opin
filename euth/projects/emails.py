from adhocracy4 import emails


class ModeratorAddedEmail(emails.Email):
    template_name = 'notify_new_moderator'

    def get_recipients(self):
        self.kwargs['user']
