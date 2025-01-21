import os
from utils import SCORES_FILE_NAME, BAD_RETURN_CODE  # Import constants from utils.py

# Constants
POINTS_OF_WINNING = lambda difficulty: (difficulty * 3) + 5  # Points calculation based on difficulty

def add_score(difficulty):
    """
    Adds points to the current score based on the difficulty level.
    If the score file doesn't exist, it will be created.

    :param difficulty: The difficulty level of the game (1-5)
    :return: Returns the updated score, or a bad return code if an error occurs
    """
    try:
        # Calculate points based on the difficulty
        points = POINTS_OF_WINNING(difficulty)

        # Check if the scores file exists
        if os.path.exists(SCORES_FILE_NAME):
            # Read the current score from the file
            with open(SCORES_FILE_NAME, "r") as file:
                current_score = int(file.read().strip())
        else:
            # If the file doesn't exist, start with 0 score
            current_score = 0

        # Add the points to the current score
        updated_score = current_score + points

        # Save the updated score to the file
        with open(SCORES_FILE_NAME, "w") as file:
            file.write(str(updated_score))

        # Return the updated score
        return updated_score

    except Exception as e:
        # In case of any error, print the error and return the bad return code
        print(f"Error adding score: {e}")
        return BAD_RETURN_CODE
