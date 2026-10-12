from dataclasses import dataclass


@dataclass
class Text:
    text: str
    rot_type: int
    encrypted: bool


class Buffer:
    def __init__(self):
        self.__data: list[Text] = []

    @property
    def data(self):
        return self.__data

    def add(self, text: Text) -> None:
        self.__data.append(text)

    def extend(self, text: list[Text]) -> None:
        self.__data.extend(text)

    def clear(self) -> None:
        self.__data.clear()

    def show(self) -> None:
        for element in self.__data:
            print(element)
