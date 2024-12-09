def welcome():
    # Prompt the user to enter their name
    name = input("Please enter your name: ")

    # Display the personalized welcome message
    print(f"Hi {name} and welcome to the World of Games: The Epic Journey")


# Call the function to test it


def start_play():
    # Display the list of games
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.")
    print("2. Guess Game - guess a number and see if you chose like the computer.")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS.")

    # Get the user's choice
    game_choice = input("Enter the number of the game you want to play (1-3): ")

    # Validate the game choice
    if game_choice not in {"1", "2", "3"}:
        print("Invalid choice. Please enter a number between 1 and 3.")
        return

    # difficulty level
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




