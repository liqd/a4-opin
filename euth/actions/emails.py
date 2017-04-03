from django.contrib import auth

from adhocracy4 import emails

User = auth.get_user_model()


class NotifyCreatorEmail(emails.UserNotification):
    template_name = 'euth_actions/emails/notify_creator'
    user_attr_name = 'actor'

    def get_receivers(self):
        action = self.object
        if hasattr(action.target, 'creator'):
            creator = action.target.creator
            if creator.get_notifications and not creator == action.actor:
                return [creator]
        return []


class NotifyModeratorsEmail(emails.ModeratorNotification):
    template_name = 'euth_actions/emails/notify_creator'

    def get_receivers(self):
        return [r for r in super().get_receivers()
                if r.get_notifications and r != self.object.actor]


class NotifyFollowersOnPhaseIsOverSoonEmail(emails.Email):
    template_name = 'euth_actions/emails/notify_followers_over_soon'

    def get_receivers(self):
        return User.objects.filter(
            follow__project=self.object.project,
            follow__enabled=True,
            get_notifications=True
        )


class NotifyFollowersOnNewIdeaCreated(emails.Email):
    template_name = 'euth_actions/emails/notify_followers_new_idea'

    def get_receivers(self):
        return User.objects.filter(
            follow__project=self.object.project,
            follow__enabled=True,
            get_notifications=True
        )
