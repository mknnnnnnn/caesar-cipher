import sys

from buffer import Buffer, Text
from cipher import CipherFactory
from file_handler import FileHandler
from menu import Menu


class Manager:
    def __init__(self, buffer: Buffer):
        self.buffer = buffer
        self.extend_dict = False
        self.options = {
            "1": self.load_to_buffer_from_file,
            "2": self.save_to_file_from_buffer,
            "3": self.clear_buffer,
            "4": self.show_buffer,
            "5": lambda: self.rot(13),
            "6": lambda: self.rot(47),
            "7": self.exit,
        }

    def menu_options(self) -> None:
        while True:
            Menu.show()
            choice = Menu.get_choice()
            if choice not in self.options:
                print(f"Invalid choice {choice}")
                continue

            self.options.get(choice)()

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

    def single_text_rot(self, rot_type: int, operation: bool = True) -> None:
        if not isinstance(operation, bool):
            raise TypeError("Operation should be bool type")

        input_text = Menu.insert_text()
        cipher = CipherFactory.create(rot_type)

        method = cipher.encode if operation else cipher.decode

        result = method(input_text)

        self.buffer.add(Text(result, rot_type, operation))

    def whole_buffer_rot(self, rot_type: int, operation: bool = True) -> None:
        if not isinstance(operation, bool):
            raise TypeError("Operation should be bool type")

        cipher = CipherFactory.create(rot_type)
        method = cipher.encode if operation else cipher.decode

        for i, data in enumerate(self.buffer.data):
            if data.encrypted != operation and data.rot_type == rot_type:
                text = method(data.text)
                self.buffer.data[i] = Text(text, rot_type, operation)

    def rot(self, rot_type: int) -> None:

        options = {
            "1": lambda: self.single_text_rot(rot_type, True),
            "2": lambda: self.single_text_rot(rot_type, False),
            "3": lambda: self.whole_buffer_rot(rot_type, True),
            "4": lambda: self.whole_buffer_rot(rot_type, False),
        }
        Menu.show_rot_options()
        choice = Menu.get_choice()

        if choice not in options:
            print("Choose correct choice")

        options.get(choice)()

    def exit(self):
        sys.exit()
