from pytest_factoryboy import register

from . import factories

register(factories.RegistrationFactory)
register(factories.ResetFactory)
