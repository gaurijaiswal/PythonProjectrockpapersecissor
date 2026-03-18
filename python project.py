import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def decide_winner(user, computer):
    if user == computer:
        return "Draw"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You Win"
    else:
        return "You Lose"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("\nEnter rock, paper, or scissors (or 'exit' to quit): ").lower()

        if user_choice == "exit":
            print("\nGame Over!")
            print("Final Score -> You:", user_score, "Computer:", computer_score)
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input! Try again.")
            continue

        computer_choice = get_computer_choice()

        print("Computer chose:", computer_choice)

        result = decide_winner(user_choice, computer_choice)
        print(result)

        if result == "You Win":
            user_score += 1
        elif result == "You Lose":
            computer_score += 1

        print("Score -> You:", user_score, "Computer:", computer_score)

# Run the game
play_game()