import rules

from euth.phases import content

from . import models


@rules.predicate
def is_active_phase(project, phase_type):
    return[content.active_phase.type] == phase_type


@rules.predicate
def is_moderator(user, project):
    return user in project.moderators.all()


@rules.predicate
def is_member(user, project):
    return (
        (project.is_public and user.is_authenticated())
        or user in project.participants.all())


def has_feature_active(project, model, feature):
    if not project.active_phase:
        return False
    else:
        return project.active_phase.has_feature('crud', model)


@rules.predicate
def is_owner(user, item):
    return item.creator == user


@rules.predicate
def can_modify_idea(user, idea):
    return (
        is_moderator(user, idea.project) | (
            is_owner(user, idea) &
            is_member(user, idea.project) &
            has_feature_active(idea.project, models.Idea, 'crud')))


@rules.predicate
def can_create_idea(user, module):
    return (
        is_moderator(user, module.project) | (
            is_member(user, module.project) &
            has_feature_active(module.project, models.Idea, 'crud')))

rules.add_perm('ideas.modify_idea', can_modify_idea)
rules.add_perm('ideas.create_idea', can_create_idea)
