from adhocracy4 import emails


class InviteEmail(emails.ExternalNotification):
    template_name = 'invite'


class RequestReceivedEmail(emails.ModeratorNotification):
    template_name = 'request_received'


class RequestAcceptedEmail(emails.UserNotification):
    template_name = 'request_accepted'


class RequestDeniedEmail(emails.UserNotification):
    template_name = 'request_denied'
