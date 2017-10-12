from adhocracy4 import emails


class InviteEmail(emails.ExternalNotification):
    template_name = 'euth_memberships/emails/invite'


class RequestReceivedEmail(emails.ModeratorNotification):
    template_name = 'euth_memberships/emails/request_received'


class RequestAcceptedEmail(
        emails.UserNotification,
        emails.mixins.SyncEmailMixin
):
    template_name = 'euth_memberships/emails/request_accepted'


class RequestDeniedEmail(
        emails.UserNotification,
        emails.mixins.SyncEmailMixin
):
    template_name = 'euth_memberships/emails/request_denied'
