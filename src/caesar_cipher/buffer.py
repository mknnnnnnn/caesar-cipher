from dataclasses import asdict, dataclass


@dataclass
class Text:
    text: str
    rot_type: int
    encrypted: bool

    def __str__(self):
        return f"Text: {self.text}, ROT: {self.rot_type}, Encrypted: {self.encrypted}"


class Buffer:
    def __init__(self) -> None:
        self.__data: list[Text] = []

    @property
    def data(self) -> list[Text]:
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

    def to_dict(self) -> list[dict[str, str | int | bool]]:
        return [asdict(data) for data in self.__data]
