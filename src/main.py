import sys

from .caesar_cipher.buffer import Buffer
from .caesar_cipher.manager import Manager


def main():
    try:
        buffer = Buffer()
        manager = Manager(buffer=buffer)
        manager.menu_options()
    except Exception:  # noqa: BLE001
        print("\n Unexpected error. Try again")
        sys.exit(0)


if __name__ == "__main__":
    main()
