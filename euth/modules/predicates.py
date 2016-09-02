import rules

from euth.projects.predicates import is_member, is_moderator


@rules.predicate
def is_context_moderator(user, item):
    return is_moderator(user, item.project)


@rules.predicate
def is_context_member(user, item):
    return is_member(user, item.project)


@rules.predicate
def is_owner(user, item):
    return item.creator == user
