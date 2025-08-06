"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    if x_count == o_count:
        return X  # X starts first
    elif x_count > o_count:
        return O  # O plays next if X has played
    else:
        raise ValueError("Invalid board state: X and O counts are inconsistent.")


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                actions_set.add((i, j))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if not (0 <= i < 3 and 0 <= j < 3):
        raise ValueError("Invalid action: Indices out of bounds.")
    if board[i][j] is not EMPTY:
        raise ValueError("Invalid action: Cell is not empty.")
    new_board = [row.copy() for row in board]
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    return None  # No winner yet


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0  # No winner, game is a draw or still ongoing


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return utility(board)  # Return score, not None

    current_player = player(board)
    best_action = None

    if current_player == X:
        best_value = -math.inf
        for action in actions(board):
            value = minimax(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
        return best_action if best_action is not None else best_value
    else:
        best_value = math.inf
        for action in actions(board):
            value = minimax(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action
        return best_action if best_action is not None else best_value