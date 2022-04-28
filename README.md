# ABOUT THIS PROJECT:

Built this project because I was tired of writing college assignments. Took 3 Hours to complete this project. This Project will convert the given text file into images (like written in A4 sheet) and the images will be found in the 'outputs' directory. The 'fonts' directory holds the 'truetype' fonts required to get the handwritten looking fonts.

Note: The 'outputs' directory will get cleared automatically after running the 'script.py' file.


# REQUIREMENTS:

1. python3 (Want to install? Click [here](https://www.python.org/downloads/))
2. git (requires installation)
3. pillow (requires installation)
4. textwrap (inbuilt)
5. os (inbuilt)
6. glob (inbuilt)
7. sys (inbuilt)
8. pathlib (inbuilt)


# USAGE:

1. Git clone this repository using the command

        git clone https://github.com/rhitabratakarar/TextToHandwriting.git

2. Use this command to change into 'TextToHandwriting' directory

        cd TextToHandwriting

3. Use the command to install dependencies

        Windows: python -m pip install -r requirements.txt

        Ubuntu: python3 -m pip install -r requirements.txt

4. The text that needs to convert can be present in 'Text.txt' file in the 'TextToHandwriting' directory or maybe in other text file.

5. To execute the script using the command respective to the operating system

        Windows: python script.py

        Ubuntu: python3 script.py

**Note**: The 'outputs' directory gets cleared everytime 'script.py' gets executed.


# ADDITIONAL CONFIGURATIONS:

1. In the 'script.py' file, variables named:

        CHR_READ_LMT: Determines how many characters will be present in a single image.

        WRAPPED_WIDTH: Determines the numbers of characters that will be present in a single line

        FONT_SIZE: The font size of every character in a single image.

        CHOSEN_FONT: The font to use in the image.

In order to add additional font, download the 'ttf' font and place it into 'fonts' directory and change the variable `CHOSEN_FONT` to the fullname of the font.
