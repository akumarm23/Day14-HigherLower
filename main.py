from art import logo, vs
from data import data
import random
import os

def format_data(account):
    """Format account data and return the printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name} is a {account_desc} from {account_country}\n"

def check_answer(guess, a_follow, b_follow):
    """Check if the user's guess is correct based on followers count."""
    if a_follow > b_follow:
        return guess == 'a'
    else:
        return guess == 'b'

# Display the game logo
print(logo)

# Initialize score and set game continuation flag
score = 0
game_continue = True

# Initialize account_b with a random account from data
account_b = random.choice(data)

while game_continue:
    # Move the current account_b to account_a and select a new account_b
    account_a = account_b
    account_b = random.choice(data)
    
    # Ensure that account_a and account_b are different
    while account_a == account_b:
        account_b = random.choice(data)

    # Display the two accounts for comparison
    print(f"Compare A:  {format_data(account_a)}")
    print(vs)
    print(f"Compare B:  {format_data(account_b)}\n")

    # Get user input for their guess
    guess = input("Who has more followers? A or B: ").lower()

    # Get followers count for accounts A and B
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    # Clear the console screen
    os.system('clear' if os.name == 'posix' else 'cls')
    print(logo)

    # Check if the user's guess is correct and update the score
    if check_answer(guess, a_followers, b_followers):
        score += 1
        print(f"\nCORRECT! Your Current Score is {score}\n")
    else:
        # End the game if the guess is incorrect
        game_continue = False
        print(f"\nSORRY :( Your Final Score is {score}\nGAME ENDED\n")

# END OF CODE ####################################
