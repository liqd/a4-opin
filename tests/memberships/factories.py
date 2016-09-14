import factory
from tests.factories import UserFactory
from tests.projects.factories import ProjectFactory


class RequestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'euth_memberships.Request'

    creator = factory.SubFactory(UserFactory)
    project = factory.SubFactory(ProjectFactory)


class InviteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'euth_memberships.Invite'

    creator = factory.SubFactory(UserFactory)
    project = factory.SubFactory(ProjectFactory)
    email = factory.Faker('email')
