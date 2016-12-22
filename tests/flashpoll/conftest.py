from pytest_factoryboy import register

from tests.flashpoll import factories as flashpoll_factories

register(flashpoll_factories.FlashpollFactory)
