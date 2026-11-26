Tic Tac Toe - Pseudocode

The board consists of 3 * 3 cells.
There are two players.
Every player has one sign.
In every turn, a player can place their sign in one free cell.
Then it's the other player's turn.
The goal is to place your signs in a straight line, vertically, horizontally or diagonally.

Possible game states:
    - Playing
    - Player 1 wins
    - Player 2 wins
    - Draw

Main loop: While game state is Playing:
    Player picks a cell
    Update board
    Check for game over
    Switch player
Output game result

Update board:
    Output board with signs

Check for game over:
    If one of the following contains only signs of one player: set game state to current player wins
        - Check all rows
        - Check all columns
        - Check both diagonals

    If all cells are filled:
        Set game state to Draw
