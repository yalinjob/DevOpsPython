import random
import time


# Function to generate a sequence of random numbers
def generate_sequence(difficulty):
    # Generate a list of random numbers between 1 and 101, length equal to difficulty
    return [random.randint(1, 101) for _ in range(difficulty)]


# Function to get a list of numbers from the user
def get_list_from_user(difficulty):
    # Prompt user to input numbers, split into a list, and convert to integers
    user_input = input(f"Enter {difficulty} numbers separated by space: ")
    return [int(x) for x in user_input.split()]


# Function to compare two lists and check if they are equal
def is_list_equal(list1, list2):
    return list1 == list2


# Main game function
def play(difficulty):
    # Generate the random sequence
    sequence = generate_sequence(difficulty)

    # Display the sequence briefly (0.7 seconds)
    print("Memorize this sequence:")
    print(sequence)
    time.sleep(0.7)  # Wait for 0.7 seconds

    # Clear screen after the display time (this part may differ based on environment)
    print("\033c", end="")  # This works on Unix-based systems to clear the terminal

    # Get the user's input
    user_sequence = get_list_from_user(difficulty)

    # Compare the user's input with the generated sequence
    if is_list_equal(sequence, user_sequence):
        print("You win!")
        return True
    else:
        print(f"You lose! The correct sequence was {sequence}")
        return False


