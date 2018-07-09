import uuid

from adhocracy4.dashboard.components.forms import ModuleDashboardForm

from . import services


class FlashpollSettingsForm(ModuleDashboardForm):

    def __init__(self, *args, **kwargs):
        self.module = kwargs['instance']
        kwargs['instance'] = self.module.settings_instance
        super().__init__(*args, **kwargs)
        if not self.module.settings_instance.key == '':
            self.pollid = self.module.settings_instance.key
        elif 'key' in self.data:
            self.pollid = self.data['key']
        else:
            self.pollid = str(uuid.uuid4())

        if 'key' in self.fields:
            services.fp_context_data(self)

    def save(self, commit=True):
        project = self.module.project
        data = self.data
        services.send_to_flashpoll(data, project)
        super().save(commit)
        return self.module

    def get_project(self):
        return self.module.project

    # class Meta:
    #     model = models.Flashpoll
    #     fields = ['key']
    #     required_for_project_publish = ['key']
    #     widgets = models.Flashpoll.widgets()
