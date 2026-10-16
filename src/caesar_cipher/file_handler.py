import json
from pathlib import Path


class FileHandler:
    def __init__(self, path: Path):
        self.path = path

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        if not isinstance(value, Path):
            raise TypeError("Insert correct path")

        self._path = value

    def load_from_file(self) -> list[dict] | str:
        try:
            if self.path.exists():
                with open(self.path, "r") as file:
                    data = json.load(file)
                return data
            else:
                with open(self.path, "w") as file:
                    json.dump([], file)
        except PermissionError as e:
            raise e("Permission error")
        except json.JSONDecodeError as e:
            raise e("Invalid JSON file")

    def save_to_file(self, data: list[dict]) -> None | str:
        try:
            with open(self.path, "w") as file:
                json.dump(data, file, indent=4)
        except PermissionError as e:
            raise e("Permission error")
