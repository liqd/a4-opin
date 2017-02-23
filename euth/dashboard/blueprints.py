from collections import namedtuple

from django.utils.translation import ugettext_lazy as _

from euth.documents import phases as documents_phases
from euth.flashpoll import phases as flashpoll_phases
from euth.ideas import phases as ideas_phases
from euth.maps import phases as map_phases

ProjectBlueprint = namedtuple(
    'ProjectBlueprint', [
        'title', 'description', 'content', 'image', 'settings_model',
    ]
)

blueprints = [
    ('ideas-collection-1',
     ProjectBlueprint(
         title=_('Brainstorming'),
         description=_('Collect ideas, questions and input concerning '
                       'a problem or a question from a wide array of people.'),
         content=[
             ideas_phases.CollectPhase(),
         ],
         image='images/brainstorming.png',
         settings_model=None,
     )),
    ('MapIdeas',
     ProjectBlueprint(
         title=_('Spatial Brainstorming'),
         description=_('Collect ideas, questions and input concerning a '
                       'problem or a question from a wide array of people.'),
         content=[
             map_phases.CollectPhase(),
         ],
         image='images/spatial_brainstorming.png',
         settings_model=('euth_maps', 'AreaSettings'),
     )),
    ('ideas-collection-2',
     ProjectBlueprint(
         title=_('Idea Challenge'),
         description=_('Run a challenge and find the best ideas to solve '
                       'a particular problem.'),
         content=[
             ideas_phases.CollectPhase(),
             ideas_phases.RatingPhase(),
         ],
         image='images/challenge.png',
         settings_model=None,
     )),
    ('map-ideas-challenge',
     ProjectBlueprint(
         title=_('Spatial Idea Challenge'),
         description=_('Run a challenge concerning a certain area or space in '
                       'your community and find the best ideas to solve a '
                       'particular problem.'),
         content=[
             map_phases.CollectPhase(),
             map_phases.RatingPhase(),
         ],
         image='images/spatial_challenge.png',
         settings_model=('euth_maps', 'AreaSettings'),
     )),
    ('agenda-setting',
     ProjectBlueprint(
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
     )),
    ('commenting-text',
     ProjectBlueprint(
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
     )),
    ('flashpoll',
     ProjectBlueprint(
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
     )),
]


class BlueprintMixin():
    @property
    def blueprint(self):
        return dict(blueprints)[self.kwargs['blueprint_slug']]
