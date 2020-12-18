import random
from board_printer import print_board
import time
from exceptions import InvalidMoveException
from victory_check import check_victory


def run_game(name_1, name_2, function_1, function_2, print_output=True, move_duration=0):
    '''Runs the game
    (param) name_1 (string): The name of the first player
    (param) name_1 (string): The name of the second player
    (param) function_1 (function): The logic function of the first player
    (param) function_2 (function): The logic function of the second player
    (return) Will be 0 for no win, 1 for player 1 win, or 2 for player 2 win'''
    # Create the board
    board = [[0] * 6 for i in range(7)]

    # Possibly swap the order
    swap_order = random.randint(0, 1)
    if swap_order:
        (name_1, name_2) = (name_2, name_1)
        (function_1, function_2) = (function_2, function_1)

    if print_output:
        print(name_1 + " will go first")
        print_board(board)
        time.sleep(move_duration)

    winner = 0

    while winner == 0:
        # Process turn of player 1
        process_turn(function_1)


def process_turn(board, move_logic, player_number):
    '''Processes a turn for the specified player
    (param) board ([[int]*6]*7): A board
    (param) move_logic (function) The function which returns which column the token is to be added to
    (param) player_number The number of the player'''

    # Get the index of the column selected by the move logic
    i_column_add = move_logic(board, player_number)

    # Check the value provided is valid
    if type(i_column_add) != int:
        raise InvalidMoveException("The provided column index was {} when it should be an integer".format(i_column_add))

    if i_column_add < 0 or i_column_add > 6:
        raise InvalidMoveException("The provided column index was {} when it should be between 0 and 6, inclusive".format(i_column_add))

    add_token(board, i_column_add, player_number)

    return check_victory(board)


def add_token(board, i_column, player_number):
    '''Adds a token to the specified column of the board
    (param) board ([[int]*6]*7): A board
    (param) i_column (int): The index of the board the token is to be added to
    (param) player_number (int): The number of the player whose token is to be added
    '''

    for i_row in range(6):
        if not board[i_column][i_row]:
            board[i_column][i_row] = player_number
            break
    else:
        raise InvalidMoveException("The provided column index was {}, which corresponded to a full column".format(i_column))