from django import forms
from django.utils.translation import ugettext as _


class GetSuggestionForm(forms.Form):
    aim_choices = [
        {
            'value': 1,
            'label': _('to get innovative to create and gather new ideas '
                       'or visions.'),
            'example': [_('(Urban) planning processes'),
                        _('Develop concepts or guiding principles')]
        }, {
            'value': 2,
            'label': _('to gather feedback on a topic and discuss it in '
                       'greater detail.'),
            'example': [_('Discuss existing concepts or plans'),
                        _('Develop solutions for existing problems')]
        }, {
            'value': 3,
            'label': _('to design a place or an event.'),
            'example': [_('(Urban) planning processes'),
                        _('Set the agenda of an event')]
        }, {
            'value': 4,
            'label': _('to learn about what people like most.'),
            'example': [_('Majority votes'), _('Opinion polls')]
        }, {
            'value': 5,
            'label': _('to run a competition.'),
            'example': [_('All sorts of competitions, '
                          'like idea contests etc.')]
        }, {
            'value': 6,
            'label': _('to work collaboratively on a text document.'),
            'example': [_('Draft or revise statutes, articles, or charters'),
                        _('Involve different authors in writing a shared '
                          'text')]
        },
    ]
