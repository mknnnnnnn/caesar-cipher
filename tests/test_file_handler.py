from pathlib import Path
from unittest import mock
from unittest.mock import mock_open

import pytest

from src.caesar_cipher.file_handler import FileHandler


def test_should_set_correct_path():
    path = Path("data.json")
    file_handler = FileHandler(path=path)

    assert file_handler.path == Path(path)


@pytest.mark.parametrize("path", ["data.json", "text", 10])
def test_should_raise_error_when_path_is_incorrect(path):
    with pytest.raises(expected_exception=TypeError):
        FileHandler(path)


def test_should_save_data_to_file():
    path = Path("data.json")
    data = [{"data": "text"}]
    m = mock_open()
    with (
        mock.patch("builtins.open", m),
        mock.patch("src.caesar_cipher.file_handler.json.dump") as mock_json_dump,
    ):
        FileHandler(path).save_to_file(data=data)

    m.assert_called_once_with(path, "w")
    mock_json_dump.assert_called_once_with(data, m.return_value, indent=4)
