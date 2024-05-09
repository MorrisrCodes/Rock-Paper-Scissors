import random as rd

print('Welcome to Rock Paper Scissors')
gamemode = input('Do you want to play against the computer or a friend? Enter 1 for computer and 2 for friend: ')
 
play = True

if gamemode == '1':
    while play == True:
        player1move = input('Choose rock, paper, or scissors: ')
        player2move = rd.choice(['rock', 'paper', 'scissors'])
        print(f'Player 2 chose {player2move}')
        if player1move == 'rock' and player2move == 'scissors':
            print('You win!')
        elif player1move == 'rock' and player2move == 'paper':
            print('Player 2 wins')
        elif player1move == 'paper' and player2move == 'rock':
            print('You win!')
        elif player1move == 'paper' and player2move == 'scissors':
            print('Player 2 wins')
        elif player1move == 'scissors' and player2move == 'rock':
            print('Player 2 wins')
        elif player1move == 'scissors' and player2move == 'paper':
            print('You win!')
        else:
            print('It is a tie')
        ifplay = input('Do you want to play again? Enter yes or no: ')
        if ifplay == 'no':
            play = False
else:
    while play == True:
        player1move = input('Choose rock, paper, or scissors: ')
        player2move = input('Choose rock, paper, or scissors: ')
        if player1move == 'rock' and player2move == 'scissors':
            print('Player 1 wins')
        elif player1move == 'rock' and player2move == 'paper':
            print('Player 2 wins')
        elif player1move == 'paper' and player2move == 'rock':
            print('Player 1 wins')
        elif player1move == 'paper' and player2move == 'scissors':
            print('Player 2 wins')
        elif player1move == 'scissors' and player2move == 'rock':
            print('Player 2 wins')
        elif player1move == 'scissors' and player2move == 'paper':
            print('Player 1 wins')
        else:
            print('It is a tie')
        ifplay = input('Do you want to play again? Enter yes or no: ')
        if ifplay == 'no':
            play = False
