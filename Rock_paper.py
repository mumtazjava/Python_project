import random  # This module is used to generate random choices for the computer

# Variables to store the number of wins for both the user and the computer
computer_win = 0
user_win = 0

# List of possible options
options = ["rock", "paper", "scissors"]

# Game loop: continues until the user types 'q' to quit
while True:
    # Ask the user to input their choice
    user_input = input("Enter 'rock', 'paper', or 'scissors' to play or 'q' to quit: ").lower()
    
    # If user wants to quit the game
    if user_input == 'q':
        break

    # If user enters something other than rock, paper, or scissors
    if user_input not in options:
        print("Invalid input. Try again.")
        continue

    # Computer randomly selects one option from the list
    computer_pick = random.choice(options)
    print("Computer picked", computer_pick + ".")

    # Check who wins
    if (user_input == "rock" and computer_pick == "scissors") or \
       (user_input == "scissors" and computer_pick == "paper") or \
       (user_input == "paper" and computer_pick == "rock"):
        print("You won!")         # User wins the round
        user_win += 1             # Increment user score
    elif user_input == computer_pick:
        print("It's a draw!")     # Same input → draw
    else:
        print("You lost!")        # Otherwise, computer wins
        computer_win += 1         # Increment computer score

# Game is over. Print the final results
print("You won", user_win, "times.")
print("The computer won", computer_win, "times.")
print("Goodbye!")

        
        
    
    

     
    