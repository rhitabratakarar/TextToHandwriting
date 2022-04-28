from pathlib import Path
from typing import TextIO


class FileOpener:
    @staticmethod
    def get_file_pointer(path: Path):
        pointer = open(path, mode="r")
        return pointer


class FileCloser:
    @staticmethod
    def close_file(file_pointer: TextIO):
        file_pointer.close()
