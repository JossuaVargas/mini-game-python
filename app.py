#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

#write 'hello world' to the console
print('hello world')

#create a function that returns random options between rock, paper, and scissors
def random_choice():
    import random
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)

#create a function that determines the winner between the user and the computer in rock, paper, scissors game
def determine_winner(user_choice, computer_choice):
    #create a variable that will be used to determine the winner
    winner = 'computer'
    #if the user and computer chose the same option, the game is a tie
    if user_choice == computer_choice:
        winner = 'tie'
    #if the user chose rock and the computer chose scissors, the user wins
    elif user_choice == 'rock' and computer_choice == 'scissors':
        winner = 'user'
    #if the user chose paper and the computer chose rock, the user wins
    elif user_choice == 'paper' and computer_choice == 'rock':
        winner = 'user'
    #if the user chose scissors and the computer chose paper, the user wins
    elif user_choice == 'scissors' and computer_choice == 'paper':
        winner = 'user'
    #return the winner
    return winner

#create a function that keep a loop running until the user chooses to quit
def play_rps():
    #create a variable that will be used to determine if the user wants to quit
    user_wants_to_quit = False
    #while the user does not want to quit, keep running the game
    while not user_wants_to_quit:
        #assign the random choice to the variable 'computer_choice'
        computer_choice = random_choice()
        #assign the user's choice to the variable 'user_choice'
        user_choice = input('rock, paper, or scissors? ')
        #validate the user's choice and prompt them to try again if it is invalid
        while user_choice not in ['rock', 'paper', 'scissors']:
            print('invalid input, try again.')
            user_choice = input('rock, paper, or scissors? ')
        #write the user's choice to the console
        print('user choice: ' + user_choice)
        #write the computer's choice to the console
        print('computer choice: ' + computer_choice)
        #assign the winner of the game to the variable 'winner'
        winner = determine_winner(user_choice, computer_choice)
        #write the winner of the game to the console
        print('winner: ' + winner)
        #prompt the user to play again or quit
        user_choice = input('play again? (yes/no) ')
        #if the user chose to quit, change the value of the variable to True
        if user_choice == 'no':
            user_wants_to_quit = True
    #write 'goodbye' to the console
    print('goodbye')

#run the game
play_rps()