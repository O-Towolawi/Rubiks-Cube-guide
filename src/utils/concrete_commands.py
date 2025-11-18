from src.abstracts.abstract_menu_command import AbstractMenuCommand


class GoToMenuCommand(AbstractMenuCommand):
    def __init__(self, menu):
        self.menu = menu

    def execute(self):
        self.menu.run()


class CloseMainMenuCommand(AbstractMenuCommand):
    def __init__(self, main_menu):
        self.main_menu = main_menu

    def execute(self):
        self.main_menu.close()


class OpenNotationsDictionaryCommand(AbstractMenuCommand):
    def __init__(self, notations_dictionary):
        self.notations_dictionary = notations_dictionary

    def execute(self):
        self.notations_dictionary.run()


class OpenScramblerCommand(AbstractMenuCommand):
    def __init__(self, scrambler):
        self.scrambler = scrambler

    def execute(self):
        self.scrambler.run()


class OpenPatternDictCommand(AbstractMenuCommand):
    def __init__(self, pattern_dictionary):
        self.pattern_dictionary = pattern_dictionary

    def execute(self):
        self.pattern_dictionary.run()
