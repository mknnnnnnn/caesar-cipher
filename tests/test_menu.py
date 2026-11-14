from pathlib import Path
from unittest import mock
from unittest.mock import call

from src.caesar_cipher.menu import Menu


def test_should_return_all_menu_options():
    with mock.patch("builtins.print") as mock_print:
        Menu.show()

    assert mock_print.call_args_list == [
        call("1. Load data from file to buffer"),
        call("2. Save data from buffer to file"),
        call("3. Clear buffer"),
        call("4. Show buffer data"),
        call("5. ROT13"),
        call("6. ROT47"),
        call("7. Exit"),
    ]


def test_should_return_all_rot_options():
    with mock.patch("builtins.print") as mock_print:
        Menu.show_rot_options()

    assert mock_print.call_args_list == [
        call("1. Encode text and add to buffer"),
        call("2. Decode text and add to buffer"),
        call("3. Encode everything in buffer"),
        call("4. Decode everything in buffer"),
    ]


def test_should_retrun_text():
    with mock.patch("builtins.input", return_value="text") as mock_input:
        result = Menu.insert_text()
        assert result == "text"

    mock_input.assert_called_once_with("Insert text to encode: ")


def test_should_return_input_path():
    with mock.patch("builtins.input", return_value="input_path.txt") as mock_input:
        result = Menu.ask_for_input_path()
        assert result == Path("input_path.txt")
    mock_input.assert_called_once_with("Insert input file path: ")


def test_should_return_ouput_path():
    with mock.patch("builtins.input", return_value="output_path.txt") as mock_input:
        assert Menu.ask_for_output_path() == Path("output_path.txt")

    mock_input.assert_called_once_with("Insert output file path: ")


def test_should_return_correct_choice():
    with mock.patch("builtins.input", return_value="1") as mock_input:
        assert Menu.get_choice() == "1"
    mock_input.assert_called_once_with("Get choice: ")
