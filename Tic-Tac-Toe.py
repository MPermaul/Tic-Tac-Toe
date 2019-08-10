#!/usr/bin/env python
# coding: utf-8

import random
import os

def clear_system():
    '''Function to clear the screen.'''
    os.system('cls')

def clear_board(board):
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    return board

def welcome_menu():
    '''Funtion that will display the rules for the Tic Tac Toe Game.'''
    # only position possible on board
    l_position = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    # tutorial board with positions
    print('=' * 50)
    print('{0:^50}'.format('Tic Tac Toe'))
    print('=' * 50)
    print('\nRules:\n')
    print('1) Player 1 will choose whether they want to be \'X\' or \'O\'.')
    print('2) Players will take turns placing their marks on the board by choosing the positions 1 thru 9.\n')
    print('\t ' + l_position[6] + ' | ' + l_position[7] + ' | ' + l_position[8])
    print('\t' + ('-' * 11))
    print('\t ' + l_position[3] + ' | ' + l_position[4] + ' | ' + l_position[5])
    print('\t' + ('-' * 11))   
    print('\t ' + l_position[0] + ' | ' + l_position[1] + ' | ' + l_position[2])
    print('\n3) Once a player has 3 of their marks in a row, they win.\n')

def display_board(board):
    '''Function that will dispaly the Tic Tac Toe board '''

    # call function to clear screen so that most updated board is displayed
    clear_system()
    
    # print statements that will display the board
    print('\t ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('\t' + ('-' * 11))
    print('\t ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('\t' + ('-' * 11))   
    print('\t ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('\n')

def player_input():
    '''Funtion that will get player input

    Return:
        player1(string): marker value chosen by player 1
        plyaer2(string): makrer value assigned to player 2
    '''   
    # get marker value and assigne it to player1 var
    player1 = input('Player 1, please pick your marker (\'X\' or \'O\'): ').upper()

    # check to make sure input is a valid marker value
    while player1 != 'X' and player1 != 'O':
        player1 = input('Please pick a valid marker (\'X\' or \'O\'): ').upper()

    # assign maker value to player2
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    # return the marker values for both players
    return (player1,player2)

def place_marker(board, marker, position):
    '''Function that will update the board list at index[postion] with value of marker
    Arguments:
        board (list): represents the board and the positions of the markers
        marker (string): represents the marker assigned to the player
        postioin (int): the location where player wants to place the marker
    '''
    board[position] = marker

def win_check(board, mark):
    '''Function that takes a board list and marker value, and checks to see if we win the game.
    
    Args:
       board (list): list with board values
        mark (string): character that will be placed on board
    '''
    # if checks go see if player won the game
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[7] == mark and board[5] == mark and board[3] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    else:
        return False

def choose_first():
    '''Function that will randomly select which player goes first.
    
    Return:
        choice (int): value for player who will go first
    '''
    # var to store randomly selected integer
    choice = random.randint(1,2)

    if choice == 1:
        return 'p1'
    else:
        return 'p2'

def space_check(board, position):
    '''Function that checks if a space on a board is open or not.

    Return:
        boolean: True if position is open, False if position is not
    '''

    if board[position] == 'X' or board[position] == 'O':
        return False
    else:
        return True

def full_board_check(board):
    '''Function that checks to see if the board is full

    Return:
        boolean: True if no positions are left on the board, False if there are
    '''

    counter = 0   

    for x in board:
        if x == 'X' or x == 'O':
            counter +=1
 
    if counter == 9:
        return True
    else:
        return False

def player_choice(board, player):
    '''Function that will prompt for a player's input and return it

    Arguments:
        board (list): the game board that is used for the game

    Return:
        position (int): the position the player chooses once checks are done
    '''
    # list that stores valid choices for the game
    validChoices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    # get input from user
    position = input('{}, which postion do you want to place your marker on?: '.format(player))

    #start a while loop to make sure choices are valid
    while True:
        # check to make sure position is valid value
        while position not in validChoices:
            position = input('{}, please enter a valid position: '.format(player))

        status = space_check(gameboard, int(position))

        if status == False:
            position = input('{}, please choose and open position: '.format(player))
        else:
            break

    return int(position)    

def replay():
    '''Function that will prompt players if they would like to play the game again

    Return:
        boolean: True if yes, False if no   
    '''
    # var to store answer from players
    answer = input('Would you like to play again? (Y/N): ')

    # check to see if answer is valid and return True/False based on answer
    while (answer.lower() != 'y') and (answer.lower() != 'n') and (answer.lower() != 'yes') and (answer.lower() != 'no'):
        answer = input('Please choose Yes(Y) or No(N): ')

    if answer.lower() == 'y' or answer.lower() == 'yes':
        clear_board (gameboard)
        return True
    else:
        print('\nThank You For Playing Tic Tac Toe!')
        return False     


# call the welcome menu
welcome_menu()

# loop that will keep game going until players no longer want to play
while True:

    # blank gameboard to start the game with placeholder to bypass index 0 of list
    gameboard = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    
    # prompt player 1 to choose marker
    p1Marker, p2Marker = player_input()

    #display_board(gameboard)
    player = choose_first()

    # check which user was randomly selected to start and set them as current player
    if player == 'p1':
        current_player = 'Player 1'
    else:
        current_player = 'Player 2'

    # loop that will keep the players going back and forth
    while True:

        # Check to see if board is full and break game loop
        if full_board_check(gameboard) == True:
            print('The Tic Tac Toe Board is Full!\n')
            print ('{0:^50}'.format('Game Over'))
            break
        # if board not full current player goes
        else:
            if current_player == 'Player 1':
                # display the status of the current board
                display_board(gameboard)

                # prompt player 1 for position to place marker and store in var
                choice = player_choice(gameboard, current_player)

                # once position is valid and checked, position will be placed on board
                place_marker(gameboard, p1Marker, choice)

                # check in player 1 wins
                if win_check(gameboard, p1Marker) == True:
                    display_board(gameboard)
                    print('{} WINS!'.format(current_player))
                    break

                # set current player to player 2
                current_player = 'Player 2'
            else:
                # display the status of the current board
                display_board(gameboard)

                # prompt player 2 for position to place marker and store in var
                choice = player_choice(gameboard, current_player)

                # once position is valid and checked, position will be placed on board
                place_marker(gameboard, p2Marker, choice)
              
                # check in player 2 wins
                if win_check(gameboard, p2Marker) == True:
                    display_board(gameboard)
                    print('{} WINS!'.format(current_player))
                    break

                # set current player to player 1
                current_player = 'Player 1'

    # prompt users if they want to play again and break the while loop if no
    if not replay():
        break
