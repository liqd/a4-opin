import factory

from adhocracy4.test.factories import ProjectFactory

from ..factories import UserFactory


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
