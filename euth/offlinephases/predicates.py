import rules

from adhocracy4.projects.predicates import is_moderator


@rules.predicate
def is_offlinephase_moderator(user, item):
    return is_moderator(user, item.phase.module.project)
