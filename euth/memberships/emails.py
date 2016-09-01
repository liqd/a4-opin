from euth.contrib import emails


class RequestReceivedEmail(emails.OpinEmail,
                           emails.ModeratorNotification):
    template_name = 'request_received'


class RequestAcceptedEmail(emails.OpinEmail,
                           emails.UserNotification):
    template_name = 'request_accepted'
