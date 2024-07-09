import random

choices = ['rock', 'paper', 'scissors']

computer = random.choice(choices)

player = None
while True:
    while player not in choices and player != 'exit':
        player = input("Rock, paper or scissors? (exit to stop) ").lower()
    if player == 'exit':
        break
    elif player == computer:
        print("Tie!")
    elif player == 'rock':
        if computer == 'paper':
            print("You lose!")
        else:
            print("You win!")
    elif player == 'paper':
        if computer == 'scissors':
            print("You lose!")
        else:
            print("You win!")
    else:  # we picked scissors
        if computer == 'rock':
            print("You lose!")
        else:
            print("You win!")
    print("computer:", computer)
    print("player:", player)
    player = None
print("Bye!")
