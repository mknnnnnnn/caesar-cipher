from unittest import mock
from unittest.mock import call

import pytest

from src.caesar_cipher.buffer import Buffer, Text

TEST_ROT_TYPE = 13
TEST_ENCRYPTED = False


@pytest.fixture
def create_text():
    def wrapper(text: str) -> Text:
        return Text(text=text, rot_type=TEST_ROT_TYPE, encrypted=TEST_ENCRYPTED)

    return wrapper


@pytest.mark.parametrize("text", ["text1", "text2", "text3"])
def test_should_add_text(text: str):
    text = Text(text=text, rot_type=TEST_ROT_TYPE, encrypted=TEST_ENCRYPTED)
    buffer = Buffer()
    buffer.add(text)
    assert buffer.data == [text]


@pytest.mark.parametrize("text_list", [(["text1", "text2"]), (["text2", "text3"])])
def test_should_extend_list(text_list: list[str]):
    buffer = Buffer()
    text_class_objects = [
        Text(text=text, rot_type=TEST_ROT_TYPE, encrypted=TEST_ENCRYPTED)
        for text in text_list
    ]

    buffer.extend(text=text_class_objects)

    assert buffer.data == text_class_objects


def test_should_clear_the_list(create_text):
    buffer = Buffer()
    text_obj = create_text(text="text")
    buffer.add(text_obj)

    assert buffer.data == [text_obj]
    buffer.clear()
    assert buffer.data == []


def test_should_print_two_values(create_text):
    buffer = Buffer()
    first_text = create_text(text="text1")
    second_text = create_text(text="text2")
    buffer.extend([first_text, second_text])

    with mock.patch("builtins.print") as mock_print:
        buffer.show()

        assert mock_print.call_args_list == [call(first_text), call(second_text)]


def test_should_return_list_of_dicts(create_text):
    buffer = Buffer()
    text_obj = create_text(text="text1")
    buffer.add(text=text_obj)
    buffer_dict = buffer.to_dict()

    assert buffer_dict == [{"text": "text1", "rot_type": 13, "encrypted": False}]


def test_should_return_empty_buffer_list():
    buffer = Buffer()
    assert buffer.data == []


def test_as_dict_method_should_return_empty_list():
    buffer = Buffer()
    buffer_dict = buffer.to_dict()

    assert buffer_dict == []
