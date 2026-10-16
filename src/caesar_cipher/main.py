from manager import Manager
from buffer import Buffer


def main():
    try:
        buffer = Buffer()
        manager = Manager(buffer=buffer)
        manager.options()
    except Exception:
        pass


if __name__ == "__main__":
    main()
