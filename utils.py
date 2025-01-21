import os
import platform

# Variables
SCORES_FILE_NAME = "Scores.txt"  # Default scores file name
BAD_RETURN_CODE = -1  # Bad return code for functions

# Functions

def screen_cleaner():
    """
    Clears the screen based on the operating system.
    This is useful when you want to clear the screen before showing the next game or after the memory game.
    """
    current_platform = platform.system()

    # Clear screen based on the platform (works on Unix-like systems, and Windows)
    if current_platform == "Windows":
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Unix/Linux/Mac
