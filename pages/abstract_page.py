import abc


class AbstractPage(object, abc.ABC):
    @abc.abstractmethod
    def __init__(self, browser, awaiter):
        self.browser = browser
        self.awaiter = awaiter
