from menu_option_builder import MenuOptionBuilder, MenuOptionBuilder
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class NotationsDictionaryMenuOptionBuilder(MenuOptionBuilder):
    def __init__(self):
        self.reset_option()

    def reset_option(self):
        return NotationsDictionaryMenuOption()

    def set_option_number(self, option_number):
        self.option_number = 1

    def set_option_name(self, option_name):
        self.option_name = "Notations dictionary"

    def set_option_trigger(self, option_trigger):
        self.option_trigger = NotationsDictionary.trigger_menu()

    def set_option_description(self, option_description):
        self.option_description = "Provides definitions for common Rubik's Cube notations."

    def build_option(self):
        option = self.option
        self.option = self.reset_option()
        return option

class NotationsDictionaryMenuOption(MenuOption):
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