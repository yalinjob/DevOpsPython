import random


def generate_number(difficulty):
    """Generates a random number between 0 and the specified difficulty."""
    return random.randint(0, difficulty)


def get_guess_from_user(difficulty):
    """Prompts the user to input a number within the range of 0 to difficulty."""
    while True:
        try:
            guess = int(input(f"Guess a number between 0 and {difficulty}: "))
            if 0 <= guess <= difficulty:
                return guess
            else:
                print(f"Invalid input. Enter a number between 0 and {difficulty}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def compare_results(secret_number, user_guess):
    """Compares the generated secret number with the user's input and returns True if they match."""
    return secret_number == user_guess


def play(difficulty):
    """Initiates the game and returns True if the user wins, False otherwise."""
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)

    if compare_results(secret_number, user_guess):
        print("Congratulations! You guessed correctly.")
        return True
    else:
        print(f"Sorry, you guessed {user_guess}, but the correct number was {secret_number}.")
        return False

