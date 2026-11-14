from pathlib import Path
from unittest import mock

import pytest

from src.caesar_cipher.buffer import Text
from src.caesar_cipher.cipher import CipherFactory
from src.caesar_cipher.manager import Manager

TEST_ROT_TYPE = 13
TEST_ENCRYPTED = False


def test_clear_data():
    buffer_mock = mock.Mock()
    manager = Manager(buffer=buffer_mock)

    with mock.patch("builtins.print") as mock_print:
        manager.clear_buffer()

    mock_print.assert_called_once_with("Buffer has been cleaned")
    buffer_mock.clear.assert_called()


def test_show_buffer_if_data_is_non_empty():
    buffer_mock = mock.Mock()
    buffer_mock.data = [
        Text(text="text", rot_type=TEST_ROT_TYPE, encrypted=TEST_ENCRYPTED)
    ]
    manager = Manager(buffer=buffer_mock)

    manager.show_buffer()

    buffer_mock.show.assert_called()


def test_show_buffer_if_data_is_empty():
    buffer_mock = mock.Mock()
    buffer_mock.data = []
    manager = Manager(buffer=buffer_mock)

    with mock.patch("builtins.print") as mock_print:
        manager.show_buffer()

    buffer_mock.show.assert_not_called()
    mock_print.assert_called_once_with("Empty list")


def test_load_to_buffer_from_file():
    buffer_mock = mock.Mock()
    manager = Manager(buffer=buffer_mock)
    manager.extend_dict = False

    with (
        mock.patch(
            "src.caesar_cipher.manager.Menu.ask_for_input_path",
            return_value=Path("data.json"),
        ) as input_path,
        mock.patch(
            "src.caesar_cipher.manager.FileHandler.load_from_file", return_value=[]
        ) as load_file_handler,
        mock.patch("builtins.print") as mock_print,
    ):
        manager.load_to_buffer_from_file()

    input_path.assert_called_once_with()
    load_file_handler.assert_called_once_with()
    buffer_mock.extend.assert_not_called()
    mock_print.assert_called_once_with("Empty list")


def test_save_to_file_from_buffer():
    buffer_mock = mock.Mock()
    data = [{"text": "tekst", "rot_type": 13, "encrypted": True}]
    buffer_mock.to_dict.return_value = data
    manager = Manager(buffer=buffer_mock)
    with (
        mock.patch(
            "src.caesar_cipher.manager.Menu.ask_for_output_path",
            return_value=Path("data.json"),
        ) as ask_for_output_path,
        mock.patch(
            "src.caesar_cipher.manager.FileHandler.save_to_file"
        ) as save_to_file,
    ):
        manager.save_to_file_from_buffer()

    ask_for_output_path.assert_called_once_with()
    buffer_mock.to_dict.assert_called_once_with()
    save_to_file.assert_called_once_with(data)


@pytest.mark.parametrize(
    "text, encryption_status, rot, expected_text",
    [(["text", True, 13, "grkg"]), ["kot", False, 47, "<@E"]],
)
def test_should_add_single_text_to_buffer(
    text: str, encryption_status: bool, rot: int, expected_text: str
):
    buffer_mock = mock.Mock()
    manager = Manager(buffer=buffer_mock)

    with (
        mock.patch(
            "src.caesar_cipher.manager.Menu.insert_text", return_value=text
        ) as insert_text,
        mock.patch(
            "src.caesar_cipher.manager.CipherFactory.create",
            return_value=CipherFactory.create(rot_type=rot),
        ) as cipher_factory,
    ):
        manager.single_text_rot(rot_type=rot, operation=encryption_status)

    insert_text.assert_called_once_with()
    cipher_factory.assert_called_once_with(rot)
    buffer_mock.add.assert_called_once_with(
        Text(text=expected_text, rot_type=rot, encrypted=encryption_status)
    )


@pytest.mark.parametrize(
    "rot_type, option, method",
    [
        ([13, "1", "single_text_rot"]),
        ([47, "1", "single_text_rot"]),
        ([13, "3", "whole_buffer_rot"]),
    ],
)
def test_should_show_rot_options(rot_type: int, option: str, method: str):
    buffer_mock = mock.Mock()
    manager = Manager(buffer=buffer_mock)
    with (
        mock.patch(
            "src.caesar_cipher.manager.Menu.show_rot_options"
        ) as show_options_mock,
        mock.patch(
            "src.caesar_cipher.manager.Menu.get_choice", return_value=option
        ) as get_choice_mock,
        mock.patch.object(manager, method) as method_mock,
    ):
        manager.rot(rot_type=rot_type)

    show_options_mock.assert_called_once_with()
    get_choice_mock.assert_called_once_with()
    method_mock.assert_called_once_with(rot_type, True)
