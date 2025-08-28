from abstract_menu_command import AbstractMenuCommand


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

class OpenPatternsMenuCommand(AbstractMenuCommand):
    def __init__(self, patterns_menu):
        self.patterns_menu = patterns_menu

    def execute(self):
        self.patterns_menu.run()

class OpenX2PatternsCommand(AbstractMenuCommand):
    def __init__(self, x2_patterns):
        self.x2_patterns = x2_patterns

    def execute(self):
        self.x2_patterns.run()