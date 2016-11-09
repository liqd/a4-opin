from euth.contrib import emails


class InviteEmail(emails.OpinEmail,
                  emails.ExternalNotification):
    template_name = 'invite'


class RequestReceivedEmail(emails.OpinEmail,
                           emails.ModeratorNotification):
    template_name = 'request_received'


class RequestAcceptedEmail(emails.OpinEmail,
                           emails.UserNotification):
    template_name = 'request_accepted'


class RequestDeniedEmail(emails.OpinEmail,
                         emails.UserNotification):
    template_name = 'request_denied'
