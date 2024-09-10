from collections import namedtuple
from enum import Enum
from enum import unique

from django.utils.translation import gettext_lazy as _

from adhocracy4.polls import phases as poll_phases

from .names import BlueprintNames


class BlueprintEnum(Enum):
    def __new__(cls, value, label):
        obj = object.__new__(cls)
        obj._value_ = len(cls.__members__) + 1
        obj._value = value
        obj.label = label
        return obj

    @property
    def value(self):
        return self._value

    @classmethod
    def get(cls, value):
        return next(m for m in cls if m._value == value)


@unique
class Aim(Enum):
    collect_ideas = (
        'collect_ideas',
        _('Create and collect new ideas or visions.'),
        [_('(Urban) planning processes'),
         _('Develop concepts or guiding principles')]
    )
    discuss_topic = (
        'discuss_topic',
        _('Gather feedback on a topic and discuss it in greater detail.'),
        [_('Discuss existing concepts or plans'),
         _('Develop solutions for existing problems')]
    )
    agenda_setting = (
        'agenda_setting',
        _('Agenda Setting'),
        [_('Set the agenda of an event, a process, a project etc.')]
    )
    design_place = (
        'design_place',
        _('Design a place.'),
        [_('(Urban) planning processes'),
         _('Small scale design projects, e.g. renew your premises')]
    )
    run_survey = (
        'run_survey',
        _('Learn about what people like most.'),
        [_('Opinion polls, majority votes etc.')]
    )
    run_competition = (
        'run_competition',
        _('Run a competition.'),
        [_('All sorts of competitions, '
           'like idea contests etc.')]
    )
    work_document = (
        'work_document',
        _('Work together with other people on a text document.'),
        [_('Draft or revise statutes, articles, charters etc.'),
         _('Involve different authors in writing a shared text')]
    )
    communitydebate = (
        'communitydebate',
        _('Find and debate topics and questions.'),
        [_('Start a discussion and moderate it'),
         _('Participants can upload documents to deepen the exchange '
           'and share information')]
    )

    def __new__(cls, value, label, examples):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.label = label
        obj.examples = examples
        return obj


@unique
class Result(BlueprintEnum):
    collect_ideas = 3, _('Collection of commented ideas')
    majority_vote = 2, _('Majority vote')
    both = 1, _('Both')


@unique
class Experience(BlueprintEnum):
    five_projects = 4, _('More than 5 participative projects')
    two_projects = 3, _('More than 2 participative projects')
    one_project = 2, _('1-2 participative projects')
    no_projects = 1, _('I have no experiences in organising '
                       'participative projects')


class Motivation(BlueprintEnum):
    high = 4, _('High motivation')
    medium = 3, _('Medium motivation')
    low = 2, _('Low motivation')
    not_found = 1, _('No motivation')
    unkown = 2, _('I don\'t know.')


@unique
class Participants(BlueprintEnum):
    few = 0, '< 25'
    some = 1, '25-50'
    many = 2, '50+'


@unique
class Duration(BlueprintEnum):
    one_weeks = 0, _('1-2 weeks')
    two_weeks = 1, _('2-4 weeks')
    four_weeks = 2, _('more than 4 weeks')


@unique
class Scope(BlueprintEnum):
    local = 0, _('Local')
    regional = 1, _('Regional')
    national = 2, _('National or international')


class Accessibility(BlueprintEnum):
    very_easy = 1, _('Very easy to access')
    easy = 2, _('Easy to access')
    hard = 3, _('Hard to access')
    very_hard = 4, _('Very hard to access')
    unkown = 3, _('I don\'t know')


ComplexityVector = namedtuple(
    'ComplexityVector', [
        'participants', 'duration', 'scope'
    ]
)


COMPLEXITY_VECTOR_AC = ComplexityVector(
    participants=(0, 0.5),
    duration=(0, 1),
    scope=(0, 0.5)
)

COMPLEXITY_VECTOR_BD = ComplexityVector(
    participants=(0, 1),
    duration=(0, 1),
    scope=(0, 1)
)

COMPLEXITY_VECTOR_E = ComplexityVector(
    participants=(0, 1 / 3),
    duration=(0, 0),
    scope=(0, 1 / 3)
)

COMPLEXITY_VECTOR_F = ComplexityVector(
    participants=(1, 1),
    duration=(0, 1),
    scope=(0, 0)
)

Requirements = namedtuple(
    'Requirements', [
        'aims', 'results', 'experience', 'motivation'
    ])


Blueprint = namedtuple(
    'Blueprint', [
        'title', 'description', 'content', 'image', 'settings_model',
        'requirements', 'complexity', 'type'
    ])


blueprints = [
    (BlueprintNames.a4_poll.value,
     Blueprint(
         title=_('Poll'),
         description=_('Run customizable, multi-step polls on OPIN to get '
                       'detailed opinions on topics from the public or your '
                       'members.'),
         content=[
             poll_phases.VotingPhase(),
         ],
         image='images/poll.png',
         settings_model=None,
         requirements=Requirements(
             aims=[Aim.run_survey],
             results=[Result.majority_vote],
             experience=Experience.no_projects,
             motivation=Motivation.not_found
         ),
         complexity=COMPLEXITY_VECTOR_E,
         type=BlueprintNames.a4_poll.name
     )),
]


fallbacks = {
    Aim.run_survey: BlueprintNames.a4_poll.value,
}
