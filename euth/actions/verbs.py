# http://activitystrea.ms/registry/verbs/

CREATE = 'create'
UPDATE = 'update'
COMPLETE = 'complete'


def all():
    items = sorted(globals().items())
    return [(value, name) for name, value in items
            if not name.startswith('_') and name != 'all']
