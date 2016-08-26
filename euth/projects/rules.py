import rules


@rules.predicate
def is_member(user, project):
    return project.has_member(user)


@rules.predicate
def is_live(user, project):
    return not project.is_draft


@rules.predicate
def is_initiator(user, project):
    return user in project.organisation.initiators.all()


rules.add_perm('projects.view_project', is_initiator | is_member & is_live)
