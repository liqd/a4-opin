from adhocracy4 import emails


class ProjectDeletedEmail(emails.InitiatorNotification):
    template_name = 'euth_dashboard/emails/project_deleted'
