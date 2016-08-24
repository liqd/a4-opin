def add_phase_to_project(project, type):
    from euth.phases import models
    phase = models.Phase.objects.create(
        name='Phase name',
        description='lorem ipsum',
        type=type,
        module=project.module_set.first())
    return phase
