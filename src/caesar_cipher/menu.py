from pathlib import Path


class Menu:
    @staticmethod
    def show() -> None:
        options = [
            "1. Wczytaj dane z pliku do bufora",
            "2. Zapisz dane z bufora do pliku",
            "3. Wyczyść bufor",
            "4. Pokaz zawartość bufora",
            "5. Zaszyfruj dane ROT13",
            "6. Odszyfruj dane ROT13",
            "7. Zaszyfruj dane ROT47",
            "8. Odszyfruj dane ROT47",
            "9. Zakończ",
        ]

        for option in options:
            print(option)

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

    @staticmethod
    def insert_text() -> str:
        return input("Insert text to encode: ")
