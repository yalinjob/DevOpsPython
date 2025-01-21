import guess_game
from memory_games import play
from currency_roulette_game import play

def welcome():
    # user to enter their name
    name = input("Please enter your name: ")

    # personalized welcome message
    print(f"Hi {name} and welcome to the World of Games: The Epic Journey")


from memory_games import play as memory_play
from guess_game import play as guess_play
from currency_roulette_game import play as currency_play
from score import add_score
from utils import screen_cleaner


def start_play():
    # List of games
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.")
    print("2. Guess Game - guess a number and see if you chose like the computer.")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS.")

    # Obtain the user's choice
    game_choice = input("Enter the number of the game you want to play (1-3): ")

    # Check the game choice
    if game_choice not in {"1", "2", "3"}:
        print("Invalid choice. Please enter a number between 1 and 3.")
        return

    # Chose the level
    try:
        difficulty_level = int(input("Choose a difficulty level (1-5): "))
        if difficulty_level < 1 or difficulty_level > 5:
            print("Invalid difficulty level. Please enter a number between 1 and 5.")
            return
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        return

    # Confirm game choice and difficulty level
    print(f"You chose game #{game_choice} with difficulty level {difficulty_level}. Enjoy playing!")

    # Clear the screen before starting the game
    screen_cleaner()

    # Call the respective game function based on the user's choice and check if they won
    if game_choice == "1":
        # Play the memory game and check if the user won
        if memory_play(difficulty_level):  # Assuming memory_play returns True if the user wins
            print("Congratulations, you won the Memory Game!")
            updated_score = add_score(difficulty_level)  # Add score based on difficulty
            print(f"Your new score is: {updated_score}")
        else:
            print("Sorry, you lost the Memory Game.")

    elif game_choice == "2":
        # Play the guess game and check if the user won (Implement the win condition for guess game)
        if guess_play(difficulty_level):  # Assuming guess_play returns True if the user wins
            print("Congratulations, you won the Guess Game!")
            updated_score = add_score(difficulty_level)  # Add score based on difficulty
            print(f"Your new score is: {updated_score}")
        else:
            print("Sorry, you lost the Guess Game.")

    elif game_choice == "3":
        # Play the currency roulette and check if the user won (Implement the win condition for currency roulette)
        if currency_play(difficulty_level):  # Assuming currency_play returns True if the user wins
            print("Congratulations, you won the Currency Roulette!")
            updated_score = add_score(difficulty_level)  # Add score based on difficulty
            print(f"Your new score is: {updated_score}")
        else:
            print("Sorry, you lost the Currency Roulette.")



