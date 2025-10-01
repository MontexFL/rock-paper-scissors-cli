import random

# Game data:

computer_moves = ["rock", "paper", "scissors"]
user_moves = {
    "r" : "rock",
    "p" : "paper",
    "s" : "scissors"
}
winning_moves = {
    "rock" : "scissors",
    "paper" : "rock",
    "scissors" : "paper"
}


# What happens when the game is run:

def game():
    introduction()
    user_wins, computer_wins = rounds()
    end_round(user_wins, computer_wins)
    

# What happens during each round:

def rounds():
    user_wins = 0
    computer_wins = 0

    while True:
        raw_input = get_raw_input()
        user_input = validate_raw_input(raw_input)
        user_move = convert_user_move(user_input)

        if user_move == "x": #-----> the user has decided to quit
            break

        computer_move = get_computer_move()
        winning_move, winner = get_round_winner(user_move, computer_move)

        #updating scores:
        if winner == "you":
            user_wins += 1
        elif winner == "I":
            computer_wins += 1

        display_round (user_move, computer_move, winning_move, winner)

    return user_wins, computer_wins


# Displaying game rules and dynamics:

def introduction():
    print ("\nPerfect, the game has begun! You will have to type 'r', 'p', or 's' (for 'rock', 'paper' or scissors) during each round. When you want to stop playing: simply type 'x' at any time. \n\nLet the game begin! Pick your move:")


# Getting the user's raw input:

def get_raw_input():
    raw_input = input ("\nInput 'r', 'p', 's' (or 'x'): ").lower().strip()
    return raw_input


# Making sure that the user's raw input is in fact 'r', 'p', 's' (or 'x'):

def validate_raw_input(raw_input):
    while True:
        if raw_input in ["r", "p", "s", "x"]:
            user_input = raw_input
            return user_input

        else:
            raw_input = input (f"\n'{raw_input}' is an invalid input, type:'r', 'p', 's' (or 'x'):").lower().strip()
    

# Converting user's (validated) input into a move:

def convert_user_move(user_input):
    user_move = user_moves.get(user_input, "x")

    return user_move


# Getting computer's move:

def get_computer_move():
    computer_move = random.choice(computer_moves)       
    return computer_move


# Establishing the winner of each round:

def get_round_winner(user_move, computer_move):
    if winning_moves[user_move] == computer_move:
        winning_move = user_move
        winner = "you"

    elif winning_moves[computer_move] == user_move:
        winning_move = computer_move
        winner = "I"
        
    else:
        winning_move = "nobody"
        winner = None
    
    return winning_move, winner


# Displaying each round:

def display_round(user_move, computer_move, winning_move, winner):
    print (f"\nComputer's move = {computer_move}")
    print (f"{user_move} vs {computer_move} = {winning_move} wins")
    if winner is None:
        print ("It's a tie, let's go again!")
    else:
        print (f"{winner} won this round, let's go again!")


# What happens when the user wants to quit:

def end_round(user_wins, computer_wins):
    print (f"\nYou won {user_wins} times.")
    print (f"I won {computer_wins} times")

    if user_wins > computer_wins:
        print ("How did you beat me???????")
    elif user_wins < computer_wins:
        print ("I knew I would win ;)")
    else:
        print ("What a tie!")

    print ("\nSee youuuuu")


# Asking the user if he/she wants to play:

def start():
    play = input ("Do you want to play a game of rock-paper-scissors against me? [y/n]: ").lower().strip()
    while True:
        if play in ["y", "yes"]:
            game()
            break
        elif play in ["n", "no"]:
            print ("\nWhat a pity :(")
            break
        else:
            play = input (f"\n'{play}' is an invalid input, type 'y' or 'n' (for 'yes' or 'no'): ")

start()
