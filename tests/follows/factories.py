import factory

from adhocracy4.test.factories import ProjectFactory
from euth.follows import models as follow_models
from tests.factories import UserFactory


class FollowFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = follow_models.Follow

    creator = factory.SubFactory(UserFactory)
    project = factory.SubFactory(ProjectFactory)
