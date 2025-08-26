from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class MenuOption(ABC):
    @abstractmethod
    def get_option_number(self):
        return self.option_number

    @abstractmethod
    def get_option_name(self):
        return self.option_name

    @abstractmethod
    def get_option_trigger(self):
        return self.option_trigger

    @abstractmethod
    def get_option_description(self):
        return self.option_description

class MenuOptionBuilder:

    @abstractmethod
    def reset_option(self):
        pass

    @abstractmethod
    def set_option_number(self, option_number):
        pass

    @abstractmethod
    def set_option_name(self, option_name):
        pass

    @abstractmethod
    def set_option_trigger(self, option_trigger):
        pass

    @abstractmethod
    def set_option_description(self, option_description):
        pass

    @abstractmethod
    def build_option(self):
        pass