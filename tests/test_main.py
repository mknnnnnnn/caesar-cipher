from unittest import mock

from src.main import main


def test_should_check_if_program_start():
    with (
        mock.patch("src.main.Buffer") as buffer_mock,
        mock.patch("src.main.Manager") as manager_mock,
    ):
        main()

    buffer_mock.assert_called_once_with()
    manager_mock.assert_called_once_with(buffer=buffer_mock.return_value)

    manager_mock.return_value.menu_options.assert_called_once_with()
