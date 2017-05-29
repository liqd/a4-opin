from euth.blueprints import blueprints as b
from euth.blueprints.views import filter_blueprints

test_blueprints = [
    ('brainstorming', b.Blueprint(
        title='brainstorming',
        description='desc',
        content=[],
        image='',
        settings_model=None,
        requirements=b.Requirements(
            aims=[b.Aim.collect_ideas],
            results=[b.Result.collect_ideas],
            experience=b.Experience.no_projects,
            motivation=b.Motivation.low
        ),
        complexity=b.COMPLEXITY_VECTOR_AC,
    )),
    ('ideacollection', b.Blueprint(
        title='ideacollection',
        description='desc',
        content=[],
        image='',
        settings_model=None,
        requirements=b.Requirements(
            aims=[b.Aim.collect_ideas, b.Aim.discuss_topic],
            results=[b.Result.collect_ideas, b.Result.both],
            experience=b.Experience.one_project,
            motivation=b.Motivation.medium
        ),
        complexity=b.COMPLEXITY_VECTOR_AC,
    )),
    ('fallback', b.Blueprint(
        title='fallback',
        description='desc',
        content=[],
        image='',
        settings_model=None,
        requirements=b.Requirements(
            aims=[b.Aim.collect_ideas],
            results=[b.Result.collect_ideas],
            experience=b.Experience.five_projects,
            motivation=b.Motivation.medium
        ),
        complexity=b.COMPLEXITY_VECTOR_AC,
    ))
]


fallbacks = {
    b.Aim.collect_ideas: 'fallback'
}


def test_blueprintsfilter_allmatch():
    data = {
        'aim': b.Aim.collect_ideas,
        'result': b.Result.collect_ideas,
        'experience': b.Experience.five_projects,
        'motivation': b.Motivation.medium,
        'participants': b.Participants.some,
        'scope': b.Scope.local,
        'duration': b.Duration.one_weeks,
        'accessibility': b.Accessibility.hard,
        'options': test_blueprints,
        'fallbacks': fallbacks
    }

    result = filter_blueprints(**data)
    assert len(result) == 3
    assert result[0][0] == 'brainstorming'
    assert result[1][0] == 'ideacollection'
    assert result[2][0] == 'fallback'


def test_blueprintsfilter_matchone():
    data = {
        'aim': b.Aim.collect_ideas,
        'result': b.Result.both,
        'experience': b.Experience.one_project,
        'motivation': b.Motivation.medium,
        'participants': b.Participants.some,
        'scope': b.Scope.local,
        'duration': b.Duration.one_weeks,
        'accessibility': b.Accessibility.hard,
        'options': test_blueprints,
        'fallbacks': fallbacks
    }

    result = filter_blueprints(**data)
    assert len(result) == 1
    assert result[0][0] == 'ideacollection'


def test_blueprintsfilter_none():
    data = {
        'aim': b.Aim.collect_ideas,
        'result': b.Result.collect_ideas,
        'experience': b.Experience.no_projects,
        'motivation': b.Motivation.not_found,
        'participants': b.Participants.some,
        'scope': b.Scope.local,
        'duration': b.Duration.one_weeks,
        'accessibility': b.Accessibility.hard,
        'fallbacks': fallbacks
    }

    result = filter_blueprints(options=test_blueprints, **data)
    assert len(result) == 1
    assert result[0][0] == 'fallback'
