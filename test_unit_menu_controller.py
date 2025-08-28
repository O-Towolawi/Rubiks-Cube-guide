from unittest.mock import patch

from menu_controller import MenuController


def test_go_to_main_menu():
    with (
        patch("main_menu.MainMenu") as mock_main_menu,
        patch("menu_controller.GoToMenuCommand") as mock_go_to_menu_command
    ):
        test_menu_controller = MenuController()
        test_menu_controller.go_to_main_menu()

        # Check MainMenu instance was created in GoToMenuCommand
        mock_go_to_menu_command.assert_called_once_with(mock_main_menu.return_value)

        # Check execute was called on GoToMenuCommand
        mock_go_to_menu_command.return_value.execute.assert_called_once()