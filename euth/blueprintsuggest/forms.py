from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class GetSuggestionForm(forms.Form):
    aim_choices = [
        {
            'value': 'collect_ideas',
            'label': _('create and gather new ideas or visions.'),
            'example': [_('(Urban) planning processes'),
                        _('Develop concepts or guiding principles')]
        }, {
            'value': 'discuss_topic',
            'label': _('gather feedback on a topic and discuss it in '
                       'greater detail.'),
            'example': [_('Discuss existing concepts or plans'),
                        _('Develop solutions for existing problems')]
        }, {
            'value': 'design_place',
            'label': _('design a place.'),
            'example': [_('(Urban) planning processes'),
                        _('Set the agenda of an event')]
        }, {
            'value': 'run_survey',
            'label': _('learn about what people like most.'),
            'example': [_('Majority votes'), _('Opinion polls')]
        }, {
            'value': 'run_competition',
            'label': _('run a competition.'),
            'example': [_('All sorts of competitions, '
                          'like idea contests etc.')]
        }, {
            'value': 'work_document',
            'label': _('work collaboratively on a text document.'),
            'example': [_('Draft or revise statutes, articles, or charters'),
                        _('Involve different authors in writing a shared '
                          'text')]
        },
    ]

    aim = forms.ChoiceField(
        choices=[(choice['value'], choice['label']) for choice in aim_choices],
        required=True
    )

    result = forms.ChoiceField(
        choices=[
            (2, _('Majority vote')),
            (1, _('Both')),
            (3, _('Weighted arguments')),
        ],
        widget=forms.RadioSelect,
        required=False,
        label=_('What is the desired outcome of the project?'),
    )

    experience = forms.ChoiceField(
        choices=[
            (1, _('More than 5 participative projects')),
            (2, _('More than 2 participative projects')),
            (3, _('1-2 partcipative projects')),
            (4, _('I have no experiences in organising participative '
                  'projects')),
        ],
        widget=forms.RadioSelect,
        required=False,
        label=_('How many participative projects have you organised and '
                'managed in the past?')
    )

    dedication = forms.ChoiceField(
        choices=[
            (1, _('High dedication')),
            (2, _('Medium dedication')),
            (3, _('Low dedication')),
            (4, _('No dedication')),
            (3, _('I don\'t know.')),
        ],
        required=False,
        widget=forms.RadioSelect,
        label=_('How dedicated are your participants?')
    )

    def clean_aim(self, *args, **kwargs):
        available_aims = [
            'collect_ideas',
            'discuss_topic',
            'design_place',
            'run_survey',
            'run_competition',
        ]

        if self.cleaned_data['aim'] not in available_aims:
            raise ValidationError(_('Invalid aim selected'))

        return self.cleaned_data['aim']
