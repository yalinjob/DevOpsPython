import random
import requests


def get_money_interval(difficulty):
    """Retrieves the current USD to ILS exchange rate and calculates an interval."""
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        usd_to_ils = data["rates"].get("ILS", 3.5)  # Default to 3.5 if API fails
    except Exception as e:
        print(f"Error fetching exchange rate: {e}")
        usd_to_ils = 3.5  # Default fallback exchange rate

    usd_amount = random.randint(1, 100)
    conversion = usd_amount * usd_to_ils
    tolerance = 10 - difficulty
    return (conversion - tolerance, conversion + tolerance), usd_amount, conversion


def get_guess_from_user(usd_amount):
    """Prompts the user to input a guess for the converted value of the given USD amount."""
    while True:
        try:
            guess = float(input(f"Guess the value of {usd_amount} USD in ILS: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def compare_results(guess, money_interval):
    """Checks if the user's guess is within the acceptable interval."""
    return money_interval[0] <= guess <= money_interval[1]


def play(difficulty):
    """Executes the Currency Roulette game and returns True if the user wins, False otherwise."""
    money_interval, usd_amount, actual_value = get_money_interval(difficulty)
    guess = get_guess_from_user(usd_amount)

    if compare_results(guess, money_interval):
        print(f"Congratulations! Your guess {guess} ILS is correct.")
        return True
    else:
        print(f"Sorry, the actual value was {actual_value:.2f} ILS. Your guess {guess} was incorrect.")
        return False
