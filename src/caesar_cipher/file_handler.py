import json
from pathlib import Path


class FileHandler:
    def __init__(self, path: Path) -> None:
        self.path = path

    @property
    def path(self) -> Path:
        return self._path

    @path.setter
    def path(self, value: Path) -> None:
        if not isinstance(value, Path):
            raise TypeError("Insert correct path")

        self._path = value

    def load_from_file(self) -> list[dict] | None:
        try:
            if self.path.exists():
                with open(self.path, "r") as file:
                    data = json.load(file)
                return data
            else:
                with open(self.path, "w") as file:
                    json.dump([], file)
                    return []
        except PermissionError as e:
            raise PermissionError("Permission error") from e
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid Json file: {self.path}") from e

    def save_to_file(self, data: list[dict]) -> None:
        try:
            with open(self.path, "w") as file:
                json.dump(data, file, indent=4)
        except PermissionError as e:
            raise PermissionError("Permission error") from e
