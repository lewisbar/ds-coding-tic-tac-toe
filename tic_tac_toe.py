# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `uv run python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# CONSTANTS

MAPPING = {'a': 0, 'b': 1, 'c': 2, '1': 0, '2': 1, '3': 2}

THREE_GROUPS = [
    ((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)), ((2,0), (2,1), (2,2)),
    ((0,0), (1,0), (2,0)), ((0,1), (1,1), (2,1)), ((0,2), (1,2), (2,2)),
    ((0,0), (1,1), (2,2)), ((0,2), (1,1), (2,0))
]

valid_inputs = []

symbols = [' ', 'X', 'O']
player_names = {1: 'Player 1', -1: 'Player 2'}

# Variables

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

current_player: int = 1  # Player 1: 1; Player 2: -1
game_state: str = 'Playing'

# FUNCTIONS

def get_player_names():
    """Asks the players for their names to use them throughout the game.
    """
    global player_names
    player_names[1] = input('Player 1, enter your name: ')
    player_names[-1] = input('Player 2, enter your name: ')

def display_board():
    """Displays the current board, the data in board, to the terminal.
    """
    print()
    print("    1   2   3  ")
    for char, row in zip(('A', 'B', 'C'), board):
        print(
            char,
            f'  {symbols[row[0]]} | {symbols[row[1]]} | {symbols[row[2]]}'
        )
        if char == 'C': break
        print('   -----------')



def update_board(field: str):
    """Inserts the player's last input field.

    Args:
        field (str): The player's input.
    """
    row = MAPPING[field[0]]
    column = MAPPING[field[1]]
    board[row][column] = current_player

def switch_player():
    """Switch the player.
    """
    global current_player
    current_player *= -1

def check_group(group) -> int:
    """Sums up the absolute values of one row, column or diagonally.

    Args:
        group (_type_): The row, column or diagonally.

    Returns:
        int: The sum of the absolute values.
    """
    result = 0
    for field in group:
        result += board[field[0]][field[1]]
    return abs(result)

def check_for_draw():
    """Checks if the board is full. This means the game ended in a draw. Otherwise, it would have ended in a win before this check happens.
    """
    return sum([abs(item) for row in board for item in row]) == 9

def validate_move(field: str):
    """Check if the move entered by the user is valid.
    """
    global valid_inputs
    return field in valid_inputs

def reset_game():
    """Resets the game's parameters.
    """
    global game_state, board, current_player, valid_inputs
    valid_inputs = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    game_state = 'Playing'
    current_player = 1
    for i in range(3):
        for j in range(3):
            board[i][j] = 0

def set_player_symbols():
    """Lets player 1 choose a symbol and assigns the other one to player 2.
    """
    symbol = input(f'{player_names[1]}, choose your symbol (X or O): ')
    if symbol.lower() == 'o':
        symbols[1] = 'O'
        symbols[2] = 'X'
    print(f'{player_names[1]}, your symbol is:', symbols[1])
    print(f'{player_names[-1]}, your symbol is:', symbols[2])

def get_next_move():
    """Asks the current player for the next move, validates the input, and applies it to the board.
    """
    while True:
        move = input(
            f'{player_names[current_player]}, make your move (e.g. A1, B2, ...): '
        ).lower()
        if validate_move(move):
            valid_inputs.remove(move)
            break
        else:
            print('Invalid input!')
    return move

def check_for_game_over():
    """Checks if either one of the players has won or there's a draw.
    """
    global game_state
    for group in THREE_GROUPS:
        if check_group(group) == 3:
            game_state = current_player
            break

    if game_state == 'Playing' and check_for_draw():
        game_state = 'Draw'

def show_result():
    """Prints the game result when the game is over.
    """
    if game_state == 'Draw':
        print("Draw!")
    else:
        print(f"{player_names[game_state]} wins!")

# The main function
def main():
    """Starts a game.
    """
    global game_state
    set_player_symbols()

    while game_state == 'Playing':
        display_board()
        print()
        field = get_next_move()
        update_board(field)
        check_for_game_over()
        switch_player()

    display_board()
    show_result()



# Tic-tac-toe game
if __name__ == "__main__":
    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
    get_player_names()
    while True:
        reset_game()
        main()
        answer = input('\nStart a new game (Y/N)? ')
        if answer.lower() != 'y': break
