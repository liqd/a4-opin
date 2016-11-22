import factory
from tests.factories import UserFactory
from tests.projects.factories import ProjectFactory

from euth.follows import models as follow_models


class FollowFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = follow_models.Follow

    creator = factory.SubFactory(UserFactory)
    project = factory.SubFactory(ProjectFactory)
