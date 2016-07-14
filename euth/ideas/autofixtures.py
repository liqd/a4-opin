from autofixture import register, AutoFixture, generators
from faker import Factory

from .models import Idea

fake = Factory.create()


class IdeaAutoFixture(AutoFixture):

    IMAGESIZES = ((1300,600),)

    field_values = {
        'name': generators.CallableGenerator(fake.company),
        'description': generators.CallableGenerator(fake.text),
        'image': generators.ImageGenerator(sizes=IMAGESIZES),
    }

register(Idea, IdeaAutoFixture)
