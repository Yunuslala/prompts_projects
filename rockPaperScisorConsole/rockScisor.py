import random

user_score = 0
computer_score = 0
draws = 0

while True:
    user_choice = input("Enter your choice (rock, paper, or scissors), or enter 'q' to quit: ")

    if user_choice.lower() == "q":
        print("Thanks for playing!")
        break

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print("Your choice:", user_choice)
    print("Computer's choice:", computer_choice)

    if user_choice in choices:
        if user_choice == computer_choice:
            print("It's a draw!")
            draws += 1
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("Congratulations! You won!")
            user_score += 1
        else:
            print("Sorry, you lost!")
            computer_score += 1
    else:
        print("Invalid input. Please enter either 'rock', 'paper', or 'scissors'.")

    print("Score: User =", user_score, "Computer =", computer_score, "Draws =", draws)
