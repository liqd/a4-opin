from django import forms

from adhocracy4.projects.models import Project
from euth.users.fields import UserSearchField


class AddModeratorForm(forms.ModelForm):
    user = UserSearchField(required=False, identifier='moderators',)

    class Meta:
        model = Project
        fields = ('user',)
