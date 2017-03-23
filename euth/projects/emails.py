from euth.contrib.emails import OpinEmail


class ModeratorAddedEmail(OpinEmail):
    template_name = 'notify_new_moderator'

    def get_receivers(self):
        return [self.kwargs['user']]
