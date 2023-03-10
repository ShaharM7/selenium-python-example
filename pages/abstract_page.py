import abc

from drivers.awaiter import Awaiter


class AbstractPage(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, browser, awaiter: Awaiter):
        self.browser = browser
        self.awaiter = awaiter
