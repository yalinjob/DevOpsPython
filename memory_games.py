import random
import time
import os
import sys

def clear_screen():
    """ Clears the terminal screen based on the environment """
    if os.getenv('TERM'):  # If TERM is set, clear the screen
        sys.stdout.write("\033[H\033[J")
        sys.stdout.flush()
    else:
        print("\n" * 100)  # Pushes old content up in PyCharm

def generate_sequence(difficulty):
    return [random.randint(1, 100) for _ in range(difficulty)]

def get_list_from_user(difficulty):
    while True:
        try:
            user_input = input(f"Enter {difficulty} numbers separated by space: ")
            return [int(x) for x in user_input.split()]
        except ValueError:
            print("Invalid input! Please enter numbers only.")

def is_list_equal(list1, list2):
    return list1 == list2

def play(difficulty):
    sequence = generate_sequence(difficulty)

    print("Memorize this sequence:")
    print(" ".join(map(str, sequence)))
    time.sleep(1)

    clear_screen()  # Clears the screen properly

    user_sequence = get_list_from_user(difficulty)

    if is_list_equal(sequence, user_sequence):
        print("You win!")
        return True
    else:
        print(f"You lose! The correct sequence was {sequence}")
        return False
