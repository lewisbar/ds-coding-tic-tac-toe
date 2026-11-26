
INPUT Player 1 symbol: X or O -> Player 2 the other
STORE Player 1's symbol in string variable
STORE Player 2's symbol in string variable
SET current_player to Player 1
SET game_state = 'Playing'
WHILE game_state == 'Playing':
    DISPLAY current Board
    OUTPUT "{current_player}, make your move:"
    INPUT field from current_player, format (A1, B2, C3 etc.)
    CALL update_board with player's input

    FOR three_group in three_groups:
        IF |SUM(three_group)|=3 THEN
            SET game_state = current_player
            BREAK
    IF game_state = 'Playing' AND SUM(|BOARD_ENTRIES|) = 9 THEN
        SET game_state = 'draw'
    SWITCH current_player

IF game_state = draw THEN
    OUTPUT "Draw!"
ELSEIF game_state = "Player 1" THEN
    OUTPUT "Player 1 wins the game."
ELSE
    OUTPUT "PLAYER 2 wins the game."



BOARD = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

mapping = {'A': 0, 'B': 1, 'C': 2, '1': 0, '2': 1, '3': 2}

def update_board(field: str):
    pass

def switch_player():
    pass

def display_board():
    pass

three_groups = [
    ((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)), ((2,0), (2,1), (2,2)),
    ((0,0), (1,0), (2,0)), ((0,1), (1,1), (2,1)), ((0,2), (1,2), (2,2)),
    ((0,0), (1,1), (2,2)), ((0,2), (1,1), (2,0))
]