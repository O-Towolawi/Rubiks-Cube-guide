from concrete_commands import GoToMenuCommand


class MenuController:
    def go_to_main_menu(self):
        from main_menu import MainMenu

        GoToMenuCommand(MainMenu()).execute()

    def go_to_notations_menu(self):
        from notations_menu import NotationsMenu

        GoToMenuCommand(NotationsMenu()).execute()

    def go_to_patterns_menu(self):
        from patterns_menu import PatternsMenu

        GoToMenuCommand(PatternsMenu()).execute()

    def go_to_scrambler_menu(self):
        from scrambler_menu import ScramblerMenu

        GoToMenuCommand(ScramblerMenu()).execute()

    def go_to_scrambler(self):
        from scrambler import Scrambler

        GoToMenuCommand(Scrambler()).execute()
