# http://activitystrea.ms/registry/verbs/

CREATE = 'create'
UPDATE = 'update'
COMPLETE = 'complete'


def all():
    return [(value, name) for name, value in globals().items()
            if not name.startswith('_') and name != 'all']
