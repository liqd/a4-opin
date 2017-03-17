from adhocracy4 import emails


class ProjectDeletedEmail(emails.InitiatorNotification):
    template_name = 'project_deleted'
