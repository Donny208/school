#Donovan Wright

#Rock Paper Scissors
#Notes: 
#rock = 1
#paper = 2
#scissors = 3
#3 beats 2
#2 beats 1
#1 beats 3

#Imports
import time
import random

#Variables

rock = 1
paper = 2
scissors = 3

names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules = {rock: scissors, paper: rock, scissors: paper}

player_score = 0
computer_score = 0

#Functions

def start():
    print('Hello, Time To Play Rock, Paper, Scissors')
    while game():
        pass
    scores()

def game():
    player = move()
    computer = random.randint(1,3)
    result(player,computer)
    return play_again()

def scores():
    global player_score, computer_score
    print('----------\nHigh Scores')
    print('Player:',player_score)
    print('Computer:',computer_score,'\n----------')

def move():
    choice = input('Rock, Paper, or Scissors?: ')
    if choice == 'Rock':
        return 1
    if choice == 'Paper':
        return 2
    if choice == 'Scissors':
        return 3

def result(p,c):
    global player_score, computer_score
    if p == 3 and c == 3:
        print('Draw! \nYou Both Picked Scissors')
    if p == 3 and c == 2:
        print('Player Wins! \n Player: Scissors | Computer: Paper')
        player_score = player_score + 1
    if p == 3 and c == 1:
        print('Computer Wins! \nPlayer: Scissors | Computer: Rock')
        computer_score = computer_score + 1
    if p == 2 and c == 3:
        print('Computer Wins! \nPlayer: Paper | Computer: Scissors')
        computer_score = computer_score + 1
    if p == 2 and c == 2:
        print('Draw! \nYou Both Picked Paper!')
    if p == 2 and c == 1:
        print('Player Wins! \nPlayer: Paper | Computer: Rock')
        player_score = player_score + 1
    if p == 1 and c == 3:
        print('Player Wins! \nPlayer: Rock | Computer: Scissors')
        player_score = player_score + 1
    if p == 1 and c == 2:
        print('Computer Wins! \nPlayer: Rock | Computer: Paper')
        computer_score = computer_score + 1
    if p == 1 and c == 1:
        print('Draw! \nYou Both Picked Rock!')
    scores()

def play_again():
    print('Wanna play again? Type game()')
