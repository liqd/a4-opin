from adhocracy4 import emails


class ProjectDeletedEmail(
        emails.InitiatorNotification,
        emails.mixins.SyncEmailMixin
):
    template_name = 'euth_dashboard/emails/project_deleted'
