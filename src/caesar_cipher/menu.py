from pathlib import Path


class Menu:
    @staticmethod
    def show() -> None:
        options = [
            "Load data from file to buffer",
            "Save data from buffer to file",
            "Clear buffer",
            "Show buffer data",
            "Encode ROT13",
            "Decode ROT13",
            "Encode ROT47",
            "Decode ROT47",
            "Exit",
        ]

        for i, option in enumerate(options):
            print(f"{i}. {option}")

    @staticmethod
    def get_choice() -> str:
        return input("Get choice: ")

    @staticmethod
    def ask_for_input_path() -> Path:
        path = Path(input("Insert input file path: "))
        return path

    @staticmethod
    def ask_for_output_path() -> Path:
        path = Path(input("Insert output file path: "))
        return path

    @staticmethod
    def insert_text() -> str:
        return input("Insert text to encode: ")
