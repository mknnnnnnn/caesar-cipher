ROT_TYPE__13 = 13
ROT_TYPE__47 = 47


class Cipher:
    @staticmethod
    def encode_rot13(text: str) -> str:
        encoded_message = ""
        for char in text:
            if char.isupper():
                encoded_message += chr(65 + (ord(char) - 65 + ROT_TYPE__13) % 26)
            elif char.islower():
                encoded_message += chr(97 + (ord(char) - 97 + ROT_TYPE__13) % 26)
            else:
                encoded_message += char
        return encoded_message

    @staticmethod
    def decode_rot13(text: str) -> str:
        return Cipher.encode_rot13(text)

    @staticmethod
    def encode_rot47(text: str) -> str:
        encode_message = ""
        for char in text:
            if 33 <= ord(char) <= 126:
                encode_message += chr(33 + (ord(char) - 33 + ROT_TYPE__47) % 94)
            else:
                encode_message += char

        return encode_message

    @staticmethod
    def decode_rot(text: str) -> str:
        return Cipher.encode_rot47(text)
