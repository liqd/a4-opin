from django import forms
from django.utils.translation import ugettext_lazy as _

from adhocracy4.projects.models import Project
from euth.users.fields import UserSearchField


class AddModeratorForm(forms.ModelForm):
    user = UserSearchField(required=False,
                           identifier='moderators',
                           help_text=_('Type in the username '
                                       'of a user you would '
                                       'like to add as moderator.'),
                           label=_('Search for username'))

    class Meta:
        model = Project
        fields = ('user',)
