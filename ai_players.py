from abc import ABC, abstractmethod
from random import choice
from typing import List


class AIPlayer(ABC):
    def __init__(self, iam: str = "O") -> None:
        """
        Initializes an AI player with a given symbol, "X" or "O".

        Args:
            iam (str): The symbol representing the AI player (default is "O").
        """
        self.iam = iam


    def _get_valid_movements(self, board: List[List[str]]) -> List[List[int]]:
        """
        Returns a list of valid movements for the current board state.

        Args:
            board (List[List[str]]): The current state of the game board.

        Returns:
            List[List[int]]: A list of valid positions on the board where a move can be made.
        """
        valid_moviments = []
        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == " ": 
                    valid_moviments.append([row+1, column+1])
        return valid_moviments

    @abstractmethod
    def define_movement(self, board: List[List[str]]) -> List[int]:
        """
        Defines the AI's movement based on the current board state.

        Args:
            board (List[List[str]]): The current state of the game board.

        Returns:
            List[int]: The row and column indices of the chosen movement.
        """
        pass



class DumbPlayer(AIPlayer):
    def define_movement(self, board: List[List[str]]) -> List[int]:
        """
        Chooses a valid movement randomly.

        Args:
            board (List[List[str]]): The current state of the game board.

        Returns:
            List[int]: The row and column indices of the chosen movement.
        """
        valid_moviments = self._get_valid_movements(board)
        movement = choice(valid_moviments)
        return movement[0], movement[1]



class MiniMaxPlayer(AIPlayer):
    def get_winner(self, board: List[List[str]]) -> str | bool:
        """
        Checks for a winner on the current board.

        Args:
            board (List[List[str]]): The current state of the game board.

        Returns:
            str: The symbol of the winning player ("X" or "O") if there is a winner.
            bool: Returns False if there is no winner.
        """
        for player in ["X", "O"]:
            for i in range(3):
                if board[0][i] == player and board[1][i] == player and board[2][i] == player:
                    return player
                if board[i][0] == player and board[i][1] == player and board[i][2] == player:
                    return player

            if board[0][0] == player and board[1][1] == player and board[2][2] == player:
                return player
            if board[0][2] == player and board[1][1] == player and board[2][0] == player:
                return player
            
        return False

    def check_draw(self, board: List[List[str]]) -> bool:
        """
        Checks if the game has ended in a draw.

        Args:
            board (List[List[str]]): The current state of the game board.

        Returns:
            bool: True if the game is a draw (no winner and no empty spaces), False otherwise.
        """
        winner = self.get_winner(board)
        if winner != 0:
            return False
        for row in board:
            if ' ' in row:
                return False
        return True
    

    def score(self, board: List[List[str]]) -> int:
        """
        Evaluates the score of the board state for the player (self.iam).

        Args:
            board (List[List[str]]): The current state of the game board.

        Returns:
            int: The score of the board state from the perspective of the current player. 0
            for a draw, +10 for a win, and -10 for a loss.
        """
        if self.check_draw(board):
            return 0
        winner = self.get_winner(board)
        if winner == self.iam:
            return 10
        elif winner in ["X", "O"]:
            return -10
        return 0
    

    def minimax(self, board: List[List[str]], active_player: str) -> int:
        """
        Recursively evaluates the final result of each play using the Minimax algorithm.

        Args:
            board (List[List[str]]): The current state of the game board.
            active_player (str): The symbol of the player whose turn it is.

        Returns:
            int: The score of the board state for the player (self.iam).
        """
        winner = self.get_winner(board)
        if winner or self.check_draw(board):
            return self.score(board)

        scores = [] 

        next_player = "X"
        if active_player == "X":
            next_player = "O"

        valid_movements = self._get_valid_movements(board)

        for move in valid_movements:
            new_board = [row[:] for row in board]
            new_board[move[0]-1][move[1]-1] = active_player
            scores.append(self.minimax(new_board, next_player))

        if active_player == self.iam:
            return max(scores)
        else:
            return min(scores)


    def define_movement(self, board: List[List[str]]) -> List[int]:
        """
        Determines the best move for the AI player using the Minimax algorithm.

        Args:
            board (List[List[str]]): The current state of the game board.

        Returns:
            List[int]: The row and column indices of the chosen movement.
        """
        scores = []
        moves = []

        next_player = "O"
        if self.iam == "O":
            next_player = "X"

        valid_movements = self._get_valid_movements(board)
        for move in valid_movements:
            new_board = [row[:] for row in board]
            new_board[move[0]-1][move[1]-1] = self.iam
            scores.append(self.minimax(new_board, next_player))
            moves.append(move)

        max_score_index = scores.index(max(scores))
        return moves[max_score_index] 







