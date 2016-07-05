from autofixture import generators
from faker import Faker


class FakeOrganisationNameGenerator(generators.Generator):

    def generate(self):
        fake = Faker()
        return fake.company()


class FakeSlugGenerator(generators.Generator):

    def generate(self):
        fake = Faker()
        return fake.slug()


class FakeNameGenerator(generators.Generator):

    def generate(self):
        fake = Faker()
        return fake.name()
