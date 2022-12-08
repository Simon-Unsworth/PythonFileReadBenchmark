import os
import sys
import multiprocessing as mp


def files_in_directory(dir: str) -> list[str]:
    return [os.path.join(dir, file) for file in os.listdir(dir)]


def read_file(path: str) -> str:
    with open(path) as file:
        return file.read()


def main(argv: list[str]) -> None:
    paths = files_in_directory(argv[1])

    with mp.Pool() as pool:
        pool.map(read_file, paths)


if __name__ == '__main__':
    try:
        main(sys.argv)
    except Exception as error:
        sys.exit(error)
