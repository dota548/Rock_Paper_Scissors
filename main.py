import random

choices = ["rock", "paper", "scissors"]

while True:
    player = input("Choose rock, paper, scissors ('quit' to stop): ").lower()

    if player == "quit":
        print("Thanks for playing")
        break

    if player not in choices:
        print("Invalid input")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if player == computer:
        print("It's a draw")
    elif (player == "rock" and computer == "scissors") or\
         (player == "paper" and computer == "rock") or\
         (player == "scissors" and computer == "paper"):
        print("you win")
    else:
        print("you lose")