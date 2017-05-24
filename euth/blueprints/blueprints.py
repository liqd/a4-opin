from collections import namedtuple
from enum import Enum, unique

from django.utils.translation import ugettext_lazy as _

from euth.documents import phases as documents_phases
from euth.flashpoll import phases as flashpoll_phases
from euth.ideas import phases as ideas_phases
from euth.maps import phases as map_phases


@unique
class Aim(Enum):
    collect_ideas = (
        'collect_ideas',
        _('Create and gather new ideas or visions.'),
        [_('(Urban) planning processes'),
         _('Develop concepts or guiding principles')]
    )
    discuss_topic = (
        'discuss_topic',
        _('Gather feedback on a topic and discuss it in greater detail.'),
        [_('Discuss existing concepts or plans'),
         _('Develop solutions for existing problems')]
    )
    design_place = (
        'design_place',
        _('Design a place.'),
        [_('(Urban) planning processes'),
         _('Set the agenda of an event')]
    )
    run_survey = (
        'run_survey',
        _('Learn about what people like most.'),
        [_('Majority votes'), _('Opinion polls')]
    )
    run_competition = (
        'run_competition',
        _('Run a competition.'),
        [_('All sorts of competitions, '
           'like idea contests etc.')]
    )
    work_document = (
        'work_document',
        _('Work collaboratively on a text document.'),
        [_('Draft or revise statutes, articles, or charters'),
         _('Involve different authors in writing a shared text')]
    )

    def __new__(cls, value, label, examples):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.label = label
        obj.examples = examples
        return obj


@unique
class Result(Enum):
    collect_ideas = 3, _('Collection of commented ideas')
    majority_vote = 2, _('Majority vote')
    both = 1, _('Both')

    def __new__(cls, value, label):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.label = label
        return obj


@unique
class Experience(Enum):
    five_projects = 4, _('More than 5 participative projects')
    two_projects = 3, _('More than 2 participative projects')
    one_project = 2, ('1-2 participative projects')
    no_projects = 1, ('I have no experiences in organising participative '
                      ' projects')

    def __new__(cls, value, label):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.label = label
        return obj


@unique
class Motivation(Enum):
    high = 5, _('High motivation')
    medium = 4, _('Medium motivation')
    low = 2, _('Low motivation')
    not_found = 1, _('No motivation')
    unkown = 3, _('I don\'t know.')

    def __new__(cls, value, label):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.label = label
        return obj


@unique
class Participants(Enum):
    few = 0, '< 25'
    some = 1, '25-50'
    many = 2, '50+'

    def __new__(cls, value, label):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.label = label
        return obj


@unique
class Duration(Enum):
    one_weeks = 0, _('1-2 weeks')
    two_weeks = 1, _('2-4 weeks')
    four_weeks = 2, _('more than 4 weeks')

    def __new__(cls, value, label):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.label = label
        return obj


@unique
class Scope(Enum):
    local = 0, _('Local')
    regional = 1, _('Regional')
    national = 2, _('National or international')

    def __new__(cls, value, label):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.label = label
        return obj


class Accessibility(Enum):
    very_easy = 1, _('Very easy to access')
    easy = 2, _('Easy to access')
    hard = 3, _('Hard to access')
    very_hard = 4, _('Very hard to access')

    def __new__(cls, value, label):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.label = label
        return obj


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
    participants=(0, 1/3),
    duration=(0, 0),
    scope=(0, 1/3)
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
        'requirements', 'complexity'
    ])


blueprints = [
    ('brainstorming',
     Blueprint(
         title=_('Brainstorming'),
         description=_('Collect ideas, questions and input concerning '
                       'a problem or a question from a wide array of people.'),
         content=[
             ideas_phases.CollectPhase(),
         ],
         image='images/brainstorming.png',
         settings_model=None,
         requirements=Requirements(
             aims=[Aim.collect_ideas, Aim.discuss_topic],
             results=[Result.collect_ideas],
             experience=Experience.no_projects,
             motivation=Motivation.not_found
         ),
         complexity=COMPLEXITY_VECTOR_AC,
     )),
    ('map-brainstorming',
     Blueprint(
         title=_('Spatial Brainstorming'),
         description=_('Collect ideas, questions and input concerning a '
                       'problem or a question from a wide array of people.'),
         content=[
             map_phases.CollectPhase(),
         ],
         image='images/spatial_brainstorming.png',
         settings_model=('a4maps', 'AreaSettings'),
         requirements=Requirements(
             aims=[Aim.design_place],
             results=[Result.collect_ideas],
             experience=Experience.no_projects,
             motivation=Motivation.not_found
         ),
         complexity=COMPLEXITY_VECTOR_AC,
     )),
    ('idea-challenge',
     Blueprint(
         title=_('Idea Challenge'),
         description=_('Run a challenge and find the best ideas to solve '
                       'a particular problem.'),
         content=[
             ideas_phases.CollectPhase(),
             ideas_phases.RatingPhase(),
         ],
         image='images/challenge.png',
         settings_model=None,
         requirements=Requirements(
             aims=[Aim.run_competition, Aim.run_survey],
             results=list(Result),
             experience=Experience.one_project,
             motivation=Motivation.low
         ),
         complexity=COMPLEXITY_VECTOR_BD,
     )),
    ('map-idea-challenge',
     Blueprint(
         title=_('Spatial Idea Challenge'),
         description=_('Run a challenge concerning a certain area or space in '
                       'your community and find the best ideas to solve a '
                       'particular problem.'),
         content=[
             map_phases.CollectPhase(),
             map_phases.RatingPhase(),
         ],
         image='images/spatial_challenge.png',
         settings_model=('a4maps', 'AreaSettings'),
         requirements=Requirements(
             aims=[Aim.design_place],
             results=list(Result),
             experience=Experience.one_project,
             motivation=Motivation.low
         ),
         complexity=COMPLEXITY_VECTOR_BD,
     )),
    ('agenda-setting',
     Blueprint(
         title=_('Agenda Setting'),
         description=_('You can involve everyone in planning a meeting. '
                       'Collect ideas for an upcoming event and let your '
                       'participants vote on the topics you want to tackle.'),
         content=[
             ideas_phases.CollectPhase(),
             ideas_phases.RatingPhase(),
         ],
         image='images/agenda_setting.png',
         settings_model=None,
         requirements=Requirements(
             aims=[Aim.collect_ideas, Aim.discuss_topic, Aim.run_survey],
             results=list(Result),
             experience=Experience.one_project,
             motivation=Motivation.low
         ),
         complexity=COMPLEXITY_VECTOR_AC,
     )),
    ('commenting-text',
     Blueprint(
         title=_('Text Review'),
         description=_('Let participants discuss individual paragraphs of a '
                       'text. This is ideal for discussing position papers or '
                       'a mission statements with many people.'),
         content=[
             documents_phases.CreateDocumentPhase(),
             documents_phases.CommentPhase(),
         ],
         image='images/text_review.png',
         settings_model=None,
         requirements=Requirements(
             aims=[Aim.work_document],
             results=None,
             experience=None,
             motivation=None
         ),
         complexity=COMPLEXITY_VECTOR_F,
     )),
    ('flashpoll',
     Blueprint(
         title=_('Poll'),
         description=_('Run customizable, multi-step polls on OPIN to get '
                       'detailed opinions on topics from the public or your '
                       'members. Via the OPIN polling app for iOS and Android '
                       'these polls are also accessible on smartphones.'),
         content=[
             flashpoll_phases.FlashpollPhase(),
         ],
         image='images/poll.png',
         settings_model=('euth_flashpoll', 'Flashpoll'),
         requirements=Requirements(
             aims=[Aim.run_survey],
             results=[Result.majority_vote],
             experience=Experience.no_projects,
             motivation=Motivation.not_found
         ),
         complexity=COMPLEXITY_VECTOR_E,
     )),
]


fallbacks = {
    Aim.collect_ideas: 'brainstorming',
    Aim.discuss_topic: 'brainstorming',
    Aim.design_place: 'map-brainstorming',
    Aim.run_survey: 'flashpoll',
    Aim.run_competition: 'agenda-setting',
    Aim.work_document: 'commenting-text'
}
