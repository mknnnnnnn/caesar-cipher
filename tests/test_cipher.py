import pytest

from src.caesar_cipher.cipher import CipherFactory


@pytest.fixture
def cipher():
    def wrapper(rot: int):
        return CipherFactory.create(rot)

    return wrapper


@pytest.mark.parametrize("text, excepted_encoded_text", [(["aaa", "nnn"])])
def test_should_return_correct_encoded_text_rot_13(
    cipher, text: str, excepted_encoded_text: str
):
    cipher_13 = cipher(13)
    assert cipher_13.encode(text) == excepted_encoded_text


# def test_should_return_correct_encoded_text_rot_47(cipher):
#     text = 'aaa'
#     cipher_13 = cipher(47)
#     assert cipher_13.encode(text) == '222'


def test_should_encode_and_decode_and_return_primary_text_rot13(cipher):
    text = "kot"
    cipher_13 = cipher(13)
    assert cipher_13.decode(cipher_13.encode(text)) == text


@pytest.mark.parametrize("text, excepted_encoded_text", [(["kot", "<@E"])])
def test_should_return_correct_encoded_text_rot_48(
    cipher, text: str, excepted_encoded_text: str
):
    cipher_47 = cipher(47)
    assert cipher_47.encode(text) == excepted_encoded_text


def test_should_encode_and_decode_and_return_primary_text_rot47(cipher):
    text = "pies"
    cipher_47 = cipher(47)
    assert cipher_47.decode(cipher_47.encode(text)) == text
