#Tic tac toe game created by Sawyer N Stakkeland

#needs 1 if/then block

#needs one while loop

#<1 function

#needs a function called main

gm_list = [1,2,3,4,5,6,7,8,9]

gm_board = (f'''{gm_list[1]} | {gm_list[2]} | {gm_list[3]}
{gm_list[4]} | {gm_list[5]} | {gm_list[6]}
{gm_list[7]} | {gm_list[8]} | {gm_list[9]}''')

def main():

    gm_list = [1,2,3,4,5,6,7,8,9]

    gm_board = (f'''{gm_list[1]} | {gm_list[2]} | {gm_list[3]}
{gm_list[4]} | {gm_list[5]} | {gm_list[6]}
{gm_list[7]} | {gm_list[8]} | {gm_list[9]}''')

    #print statements to start the game
    print(f'Velkommen til tre pa rad')
    player1 = input('Player one what is your name: ')
    player2 = input('Player 2 what is your name: ')
    print(f'{player1} you will use xs and {player2} you will use os. Let the game begin.')

    gm_loop

def gm_loop():

    print(gm_board)
    #print game board

    #player turn to choose (1-9):

    #loop