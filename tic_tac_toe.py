import os

import ai_players


class TicTacToe:
    def __init__(self) -> None:
        """
        Initializes a new game of Tic-Tac-Toe.
        
        Attributes:
            players (list): A list containing the symbols for the two players, "X" and "O".
            current_player (str): The symbol of the player who will make the next move, starting with "X".
            board (list): A 3x3 list representing the game board, initialized with empty spaces.
        """
        self.players = ["X", "O"]
        self.current_player =  self.players[0]
        self.board = [[" " for i in range(3)] for j in range(3)]


    def change_player(self) -> bool:
        """
        Switches the current player to the other player.

        Returns:
            int: Always returns 1 after the player has been changed.
        """
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]
        return True


    def get_winner(self) -> str | bool:
        """
        Checks the current state of the board to determine if there's a winner.

        Returns:
            str: The symbol of the winning player ("X" or "O") if there is a winner.
            bool: Returns False if there is no winner.
        """
        for player in ["X", "O"]:
            for i in range(3):
                if self.board[0][i] == player and self.board[1][i] == player and self.board[2][i] == player:
                    return player
                if self.board[i][0] == player and self.board[i][1] == player and self.board[i][2] == player:
                    return player

            if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
                return player
            if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
                return player
            
        return False
    

    def check_draw(self) -> bool:
        """
        Checks if the game has ended in a draw.

        Returns:
            bool: True if the game is a draw (no winner and no empty spaces), False otherwise.
        """
        winner = self.get_winner()
        if winner != 0:
            return False
        for row in self.board:
            if ' ' in row:
                return False
        return True
    

    def check_movement_is_valid(self, row: int, col: int) -> bool:
        """
        Checks if a movement to the specified row and column is valid.

        Args:
            row (int): The row index of the desired move (must be 0, 1, or 2).
            col (int): The column index of the desired move (must be 0, 1, or 2).

        Returns:
            bool: True if the move is valid (within bounds and the position is empty), False otherwise.
        """
        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            return False
        value = self.board[row][col]
        if value == " ":
            return True
        return False


    def make_movement(self, row: int, col: int) -> bool:
        """
        Makes a move on the board at the specified row and column.

        Args:
            row (int): The row index where the move will be made (must be 0, 1, or 2).
            col (int): The column index where the move will be made (must be 0, 1, or 2).

        Returns:
            int: Always returns True to indicate the move was made successfully.
        """
        self.board[row][col] = self.current_player
        return True

    

    def display_board(self) -> None:
        """
        Displays the current state of the game board in a readable format.

        Returns:
            None: This method does not return any value. It prints the board to the console.
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if j != len(self.board[0])-1:
                    print(self.board[i][j], end = " | ")
                else:
                    print(self.board[i][j])
            if i != len(self.board)-1:
                print("----------")
        print("\n\n")


    def play(self) -> None:
        """
        Initiates the game and allows the user to select the play mode.

        This method prompts the user to choose between playing with another human player or playing against an AI. 
        If the user selects to play against an AI, they are then prompted to select the difficulty level of the AI.

        Returns:
            None: This method does not return any value. It initializes the game setup based on user input.
        """
        two_players = False
        AI = False
        print("Select Play Mode:\n\t[1] 2 Players\n\t[2] Play against AI")
        play_mode=input("")
        if play_mode == "1":
            two_players = True
        elif play_mode == "2": 
            print("\nSelect Difficulty Level:\n\t[1] Easy\n\t[2] Impossible")
            difficulty_mode = input("")
            AI = True
            if difficulty_mode == "1":
                ai_player = ai_players.DumbPlayer("O")
            elif difficulty_mode == "2":
                ai_player = ai_players.MiniMaxPlayer("O")

        os.system('cls')

        while two_players:
            self.display_board()
            print(f"{self.current_player} Turn!")
            row = input("Enter row (1, 2 or 3): ")
            col = input("Enter column (1, 2 or 3): ")
            try:
                row = int(row)-1
                col = int(col)-1
            except:
                os.system('cls')
                print("Select a valid Movement please")
                continue
            
            if not self.check_movement_is_valid(row, col):
                os.system('cls')
                print("Select a valid Movement please")
                continue

            if self.make_movement(row, col):
                if self.get_winner():
                    self.display_board()
                    print(f"Player {self.get_winner()} wins!")
                    break
                elif self.check_draw():
                    self.display_board()
                    print("The game is a draw!")
                    break
                else:
                    self.change_player()
                    os.system('cls')
            else:
                os.system('cls')
                print("Select a valid Movement please")

        while AI:
            if self.current_player == "X":
                self.display_board()
                print(f"Your Turn!")
                row = input("Enter row (1, 2 or 3): ")
                col = input("Enter column (1, 2 or 3): ")
                try:
                    row = int(row)-1
                    col = int(col)-1
                except:
                    os.system('cls')
                    print("Select a valid Movement please")
                    continue
                
                if not self.check_movement_is_valid(row, col):
                    os.system('cls')
                    print("Select a valid Movement please")
                    continue

                if self.make_movement(row, col):
                    if self.get_winner():
                        self.display_board()
                        if self.get_winner() == "X":
                            print(f"You Win!")
                        elif self.get_winner() == "O": #imposible
                            print(f"You Lose!\nAI Rules!") 
                        break
                    elif self.check_draw():
                        self.display_board()
                        print("The game is a draw!")
                        break
                    else:
                        self.change_player()
                        os.system('cls')
                else:
                    os.system('cls')
                    print("Select a valid Movement please")

            else:
                row, col = ai_player.define_movement(self.board)
                try:
                    row = int(row)-1
                    col = int(col)-1
                except: #imposible
                    print("AI SELECTED WRONG MOVEMENT!")
                    continue
                
                if not self.check_movement_is_valid(row, col): #imposible
                    print("AI SELECTED WRONG MOVEMENT!")
                    continue

                if self.make_movement(row, col):
                    if self.get_winner():
                        self.display_board()
                        if self.get_winner() == "X": #imposible
                            print(f"You Win!")
                        elif self.get_winner() == "O": 
                            print(f"You Lose!\nAI Rules!") 
                        break
                    elif self.check_draw():
                        self.display_board()
                        print("The game is a draw!")
                        break
                    else:
                        self.change_player()
                else:
                    continue
    

