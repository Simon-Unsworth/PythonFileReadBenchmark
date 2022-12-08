import os
import sys


def files_in_directory(dir: str) -> list[str]:
    return [os.path.join(dir, file) for file in os.listdir(dir)]


def read_file(path: str) -> str:
    with open(path) as file:
        return file.read()


def main(argv: list[str]) -> None:
    files = files_in_directory(argv[1])
    list(map(read_file, files))


if __name__ == '__main__':
    try:
        main(sys.argv)
    except Exception as error:
        sys.exit(error)
