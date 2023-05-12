import random
from game_data import data
from replit import clear
from art import logo, vs


def person_vs_person():
    """Get data from random account"""
    return random.choice(data)


def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account['description']
    country = account["country"]
    return f"{name}, a {description} from {country}"


def more_followers(first_person, second_person):
    """Checks followers against user's guess 
    and returns True if they got it right.
    Or False if they got it wrong.""" 
    if first_person["follower_count"] > second_person["follower_count"]:
        return "A"
    else:
        return "B"


def game():
    print(logo)
    count = 0
    game_should_continue = True
    first_account = person_vs_person()
    second_account = person_vs_person()

    while game_should_continue:
        first_account = second_account
        second_account = person_vs_person()

        while first_account == second_account:
            second_account = person_vs_person()

        print(f"Compare A: {format_data(first_account)}.")
        print(vs)
        print(f"Against B: {format_data(second_account)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        correct_answer = more_followers(first_account, second_account)

        clear()
        print(logo)
        if guess == correct_answer:
            count += 1
            print(f"You're right! Current score: {count}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {count}")


game()
