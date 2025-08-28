from abc import ABC, abstractmethod


class AbstractMenuCommand(ABC):
    @abstractmethod
    def execute(self):
        pass
