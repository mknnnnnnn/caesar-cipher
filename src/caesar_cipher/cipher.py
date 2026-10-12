ROT_TYPE__13 = 13
ROT_TYPE__47 = 47

class Cipher:
    @staticmethod
    def encode_rot13(text: str) -> str:
        encoded_message = ""
        for char in text:
            if char.isspace():
                encoded_message += char
            elif char.isupper():
                encoded_message += chr(65 + (ord(char) - 65 + ROT_TYPE__13) % 26)
            else:
                encoded_message += chr(97 + (ord(char) - 97 + ROT_TYPE__13) % 26)
        return encoded_message

    @staticmethod
    def decode_rot13(text: str) -> str:
        return Cipher.encode_rot13(text)
