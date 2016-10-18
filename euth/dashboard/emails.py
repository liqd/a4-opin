from euth.contrib import emails


class ProjectDeletedEmail(emails.OpinEmail,
                          emails.InitiatorNotification):
    template_name = 'project_deleted'
