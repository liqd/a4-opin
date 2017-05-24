from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from . import blueprints


class GetSuggestionForm(forms.Form):
    aim_choices = [
        {'value': a.value, 'label': a.label, 'example': a.examples}
        for a in blueprints.Aim
    ]

    aim = forms.ChoiceField(
        choices=[(aim.value, aim.label) for aim in blueprints.Aim],
        required=True
    )

    result = forms.ChoiceField(
        choices=[(r.value, r.label) for r in blueprints.Result],
        widget=forms.RadioSelect,
        required=False,
        label=_('What is the desired outcome of the project?'),
    )

    experience = forms.ChoiceField(
        choices=[(e.value, e.label) for e in blueprints.Experience],
        widget=forms.RadioSelect,
        required=False,
        label=_('How many participative projects have you organised and '
                'managed in the past?')
    )

    motivation = forms.ChoiceField(
        choices=[(m.value, m.label) for m in blueprints.Motivation],
        required=False,
        widget=forms.RadioSelect,
        label=_('How motivated are your participants to take part in a '
                ' participative process?')
    )

    participants = forms.ChoiceField(
        choices=[(m.value, m.label) for m in blueprints.Participants],
        required=False,
        widget=forms.RadioSelect,
        label=_('How many participants do you expect for the project?')
    )

    scope = forms.ChoiceField(
        choices=[(m.value, m.label) for m in blueprints.Scope],
        required=False,
        widget=forms.RadioSelect,
        label=_('What is the scope of the project?')
    )

    duration = forms.ChoiceField(
        choices=[(m.value, m.label) for m in blueprints.Duration],
        required=False,
        widget=forms.RadioSelect,
        label=_('How long lasts the project?')
    )

    accessibility = forms.ChoiceField(
        choices=[(m.value, m.label) for m in blueprints.Accessibility],
        required=False,
        widget=forms.RadioSelect,
        label=_('How easy is it to access the project?')
    )


    def clean_aim(self, *args, **kwargs):
        try:
            return blueprints.Aim(self.cleaned_data['aim'])
        except KeyError:
            raise ValidationError(_('Invalid aim selected'))

    def _clean_optional_enum(self, name, enum):
        try:
            str_value = self.cleaned_data[name]
            if str_value:
                return enum(int(str_value))
            else:
                return None
        except (KeyError, ValueError):
            raise ValidationError(_('Invalid selection'))

    def clean_result(self, *args, **kwargs):
        return self._clean_optional_enum('result', blueprints.Result)

    def clean_experience(self, *args, **kwargs):
        return self._clean_optional_enum('experience', blueprints.Experience)

    def clean_motivation(self, *args, **kwargs):
        return self._clean_optional_enum('motivation', blueprints.Motivation)

    def clean_participants(self, *args, **kwargs):
        return self._clean_optional_enum('participants', blueprints.Participants)

    def clean_scope(self, *args, **kwargs):
        return self._clean_optional_enum('scope', blueprints.Scope)

    def clean_duration(self, *args, **kwargs):
        return self._clean_optional_enum('duration', blueprints.Duration)

    def clean_accessibility(self, *args, **kwargs):
        return self._clean_optional_enum('accessibility', blueprints.Accessibility)
