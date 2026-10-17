from abc import ABC, abstractmethod
from typing import ClassVar


class Cipher(ABC):
    @abstractmethod
    def _cipher(self, text: str) -> str:
        pass

    @abstractmethod
    def encode(self, text: str) -> str:
        pass

    @abstractmethod
    def decode(self, text: str) -> str:
        pass


class ROT13(Cipher):
    ROT_TYPE__13 = 13

    def _cipher(self, text: str) -> str:
        encoded_message = ""
        for char in text:
            if char.isupper():
                encoded_message += chr(65 + (ord(char) - 65 + self.ROT_TYPE__13) % 26)
            elif char.islower():
                encoded_message += chr(97 + (ord(char) - 97 + self.ROT_TYPE__13) % 26)
            else:
                encoded_message += char
        return encoded_message

    def encode(self, text: str) -> str:
        return self._cipher(text)

    def decode(self, text: str) -> str:
        return self._cipher(text)


class ROT47(Cipher):
    ROT_TYPE__47 = 47

    def _cipher(self, text: str) -> str:
        encode_message = ""
        for char in text:
            if 33 <= ord(char) <= 126:
                encode_message += chr(33 + (ord(char) - 33 + self.ROT_TYPE__47) % 94)
            else:
                encode_message += char

        return encode_message

    def encode(self, text: str) -> str:
        return self._cipher(text)

    def decode(self, text: str) -> str:
        return self._cipher(text)


class CipherFactory:
    _ciphers: ClassVar[dict[str, type[Cipher]]] = {"rot13": ROT13, "rot47": ROT47}

    @classmethod
    def create(cls, name: str) -> Cipher:
        cipher_class = cls._ciphers.get(name.lower())
        if cipher_class is None:
            available = ", ".join(cls._ciphers)
            raise ValueError(f"Unknown cipher '{name}'. Available: {available}")
        return cipher_class()
