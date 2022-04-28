from PIL import Image, ImageDraw, ImageFont
from components.FileManipulator import FileOpener
from components.FileManipulator import FileCloser
from pathlib import Path
from typing import TextIO
import os, sys, glob
import textwrap


A4SHEET_PATH = Path(".") / Path("a4.jpg")
CHR_READ_LMT = 2000
WRAPPED_WIDTH = 65
TEXT_TXT_PATH = Path(".") / Path("Text.txt")
OUTPUT_DIR = Path(".") / Path("outputs")

FONT_SIZE = 80
FONT_DIR = Path("fonts")
CHOSEN_FONT = "OvertheRainbow-Regular.ttf"
FULLFONTPATH = str(FONT_DIR / Path(CHOSEN_FONT))
FONT = ImageFont.truetype(FULLFONTPATH, FONT_SIZE)


def change_to_script_dir():
    os.chdir(sys.path[0])


def read_path_of_text_file() -> Path:
    path = input("Enter the absolute path of text file, leave empty for current Text.txt: ")

    if path.strip() == "":
        path = TEXT_TXT_PATH
    else:
        path = Path(path)

    return path


def get_next_characters(file: TextIO):
    while True:
        characters = file.read(CHR_READ_LMT)
        if characters:
            yield characters
        else:
            return


def get_image_filled_with(chars: str):
    with Image.open(A4SHEET_PATH) as sheet:
        draw = ImageDraw.Draw(im=sheet)
        wrapped_text = textwrap.fill(text=chars, width=WRAPPED_WIDTH)
        draw.text(xy=(10, 10), text=wrapped_text, fill="#000000", font=FONT)
    return sheet


def save_image(img, directory: Path, img_name: str) -> None:
    img.save(directory / Path(img_name))


def get_image_name_gen():
    count = 0
    while True:
        yield str(count) + ".jpg"
        count = count + 1


def generate_handwritten_images_from_text_file(file: TextIO) -> None:
    img_name = get_image_name_gen()

    for chars in get_next_characters(file):
        img = get_image_filled_with(chars)
        save_image(img, OUTPUT_DIR, next(img_name))

    del img_name


def clear_outputs_directory():
    files = glob.glob("outputs/*")
    for f in files:
        os.remove(f)


def main():
    change_to_script_dir()

    path: Path = read_path_of_text_file()

    file: TextIO = FileOpener.get_file_pointer(path)

    clear_outputs_directory()

    generate_handwritten_images_from_text_file(file)

    FileCloser.close_file(file)


if __name__ == "__main__":
    main()
