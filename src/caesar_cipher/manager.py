import sys

from buffer import Buffer, Text
from cipher import Cipher
from file_handler import FileHandler
from menu import Menu


class Manager:
    def __init__(self, buffer: Buffer):
        self.buffer = buffer
        self.extend_dict = False
        self.opt = {
            "1": self.load_to_buffer_from_file,
            "2": self.save_to_file_from_buffer,
            "3": self.clear_buffer,
            "4": self.show_buffer,
            "5": self.rot_13,
            "7": self.exit,
        }
        self.rot13_options = {
            "1": self.encode_single_text_rot13,
            "2": self.decode_single_text_rot13,
            "3": self.encode_whole_buffer_rot13,
            "4": self.decode_whole_buffer_rot13,
        }

        self.rot47_options = {}

    def options(self) -> None:
        while True:
            Menu.show()
            choice = Menu.get_choice()
            if choice not in self.opt:
                print(f"Invalid choice {choice}")
                continue

            self.opt.get(choice)()

    def load_to_buffer_from_file(self) -> None:
        path = Menu.ask_for_input_path()
        data = FileHandler(path).load_from_file()
        if self.extend_dict == False:
            if data and not isinstance(data, str):
                self.buffer.extend([Text(**text) for text in data])
                self.extend_dict = True
            else:
                print("Empty list")
        else:
            print("Data has been already loaded")

    def save_to_file_from_buffer(self):
        path = Menu.ask_for_output_path()
        FileHandler(path).save_to_file(self.buffer.to_dict())

    def clear_buffer(self) -> None:
        self.buffer.clear()
        print("Buffer has been cleaned")

    def show_buffer(self) -> None:
        if self.buffer.data:
            self.buffer.show()
        else:
            print("Empty list")

    def encode_single_text_rot13(self) -> None:
        input_text = Menu.insert_text()
        result = Cipher.encode_rot13(input_text)
        text = Text(result, 13, True)
        self.buffer.add(text)

    def decode_single_text_rot13(self) -> None:
        input_text = Menu.insert_text()
        result = Cipher.decode_rot13(input_text)
        text = Text(result, 13, False)
        self.buffer.add(text)

    def encode_whole_buffer_rot13(self, operation: bool = True) -> None:
        for i, data in enumerate(self.buffer.data):
            if not data.encrypted and data.rot_type == 13:
                text = Cipher.encode_rot13(data)
                self.buffer.data[i] = Text(text, 13, True)

    def decode_whole_buffer_rot13(self) -> None:
        for i, data in enumerate(self.buffer.data):
            if data.encrypted and data.rot_type == 13:
                text = Cipher.decode_rot13(data.text)
                self.buffer.data[i] = Text(text, 13, False)

    def rot_13(self) -> None:
        Menu.show_rot_options()
        option = Menu.get_choice()
        if option not in self.rot_options:
            print("Choose correct option")

        self.rot_options.get(option)()

    def exit(self):
        sys.exit()
