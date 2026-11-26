# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `uv run python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# CONSTANTS

MAPPING = {'A': 0, 'B': 1, 'C': 2, '1': 0, '2': 1, '3': 2}

THREE_GROUPS = [
    ((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)), ((2,0), (2,1), (2,2)),
    ((0,0), (1,0), (2,0)), ((0,1), (1,1), (2,1)), ((0,2), (1,2), (2,2)),
    ((0,0), (1,1), (2,2)), ((0,2), (1,1), (2,0))
]

symbols = [' ', 'X', 'O']

# Variables

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

current_player: int = 0
game_state: str = 'Playing'

# FUNCTIONS

def display_board():
    """Displays the current board, the data in board, to the terminal.
    """
    pass


def update_board(field: str):
    """Inserts the player's last input field.

    Args:
        field (str): The player's input.
    """
    pass

def switch_player():
    """Switch the player.
    """
    pass


# The main function
def main():
    """Starts a game.
    """
    pass


# Tic-tac-toe game
if __name__ == "__main__":
    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
    main()
