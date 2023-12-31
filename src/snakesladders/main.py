import numpy as np
from typing import Any


class SnakesAndLadders:
    """Create a SnaleAndLadders object to play the game in the console."""
    def __init__(self) -> None:
        self.board_display = np.array([["21", "S4", "23", "S3", "25"],
                                       ["S4", "S2", "L3", "L2", "S3"],
                                       ["L1", "L4", "13", "S1", "15"],
                                       ["L4", "L3", "S2", "O7", "L2"],
                                       ["01", "02", "L1", "S1", "O5"]])
        self.board_backup = self.board_display.copy()
        self.board = np.array([[21, 22, 23, 24, 25],
                               [20, 19, 18, 17, 16],
                               [11, 12, 13, 14, 15],
                               [10, 9, 8, 7, 6],
                               [1, 2, 3, 4, 5]])

    def print_board(self) -> None:
        """Print the current state of the board.
        """
        abs_pos = self.new_abs_pos(0)
        print(f"You are in the position {abs_pos}."
              "This is your current board:")
        print("+----"*5, end="+\n")
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                print("|", self.board_display[i, j], "", end="")
            print("|")
            print("+----"*5, end="+\n")

    def change_game_state(self, dice_val: int) -> bool:
        """
        Given a num of positions to move, change the board game state and
        check if the game is finished.

        Args:
            dice_val (int): Positions to move.

        Returns:
            bool: Indicates if the game is finished.
        """
        new_pos = self.new_abs_pos(dice_val)
        if new_pos > 25:
            return True
        else:
            self.move(new_pos)
            return False

    def move(self, new_pos: int) -> None:
        """
        Given a new position between 1 and 25, checks if the position is
        a stair or a ladder and updates the board.

        Args:
            new_pos (int): A new position between 1 and 25
        """
        new_index = self.get_index(self.board, new_pos)
        cell_val = self.board_display[new_index][0]

        self.board_display = self.board_backup.copy()
        self.board_display[new_index] = "XX"
        if "S" in cell_val:
            self.move_to_snake(new_index, cell_val)
        elif "L" in cell_val:
            self.move_to_ladder(new_index, cell_val)

    def move_to_snake(
            self,
            index: tuple[np.ndarray[Any, np.dtype[np.signedinteger[Any]]],
                         np.ndarray[Any, np.dtype[np.signedinteger[Any]]]],
            cell_val: str
    ) -> None:
        """
        Starting in a snake position, modifies the board with the
        resulting position.

        Args:
            index (tuple[np.ndarray[Any, np.dtype[signedinteger[Any]]],
            np.ndarray[Any, np.dtype[signedinteger[Any]]]]): Array index
            of snake position.
            cell_val (str): String identifier for the snake position.
        """
        row = index[0][0] + 1
        board_slice = self.board_display[row:, :]
        new_index = np.where(board_slice == cell_val)
        try:
            new_row = row + new_index[0][0]
        except IndexError:
            pass
        else:
            self.board_display = self.board_backup.copy()
            self.board_display[new_row, new_index[1]] = "XX"
            print("Oh no! You have fallen into a snake")

    def move_to_ladder(
        self,
        index: tuple[np.ndarray[Any, np.dtype[np.signedinteger[Any]]],
                     np.ndarray[Any, np.dtype[np.signedinteger[Any]]]],
        cell_val: str
    ) -> None:
        """
        Starting in a ladder position, modifies the board with the
        resulting position.

        Args:
            index (tuple[np.ndarray[Any,
            np.dtype[np.signedinteger[Any]]], np.ndarray[Any,
            np.dtype[np.signedinteger[Any]]]]): Array index of ladder
            position.
            cell_val (str): String identifier for the ladder position.
        """
        try:
            row = index[0][0]
        except IndexError:
            pass
        else:
            board_slice = self.board_display[:row, :]
            new_index = np.where(board_slice == cell_val)

        self.board_display = self.board_backup.copy()
        self.board_display[new_index] = "XX"
        print("You have taken a shortcut!")

    @staticmethod
    def throw_dice() -> int:
        """Select a random number between 1 and 6 (inclusive).

        Returns:
            int: The random number selected
        """
        return np.random.randint(1, 7)

    def new_abs_pos(self, dice_val: int) -> Any:
        """
        Given a number of positions to move, returns the new absolute
        position.

        Args:
            dice_val (int): Positions to move

        Returns:
            Any: New absolute position.
        """
        return dice_val + self.get_pos(self.board_display)

    def get_pos(self, board: np.ndarray[Any, np.dtype[Any]]) -> Any:
        """
        Given a game board, return the current absolute position
        of the player.

        Args:
            board (np.ndarray[Any, np.dtype[Any]]): Game board.

        Returns:
            Any: Absolute position.
        """
        if "XX" in board:
            index = np.where(self.board_display == "XX")
            return self.board[index][0]
        return 0

    def get_index(
        self,
        board: np.ndarray[Any, np.dtype[Any]],
        abs_pos: int
    ) -> tuple[np.ndarray[Any, np.dtype[np.signedinteger[Any]]],
               np.ndarray[Any, np.dtype[np.signedinteger[Any]]]]:
        """
        Given a board and an absolute position, returns the board
        indexes.

        Args:
            board (np.ndarray[Any, np.dtype[Any]]): Game board
            abs_pos (int): Absolute position.

        Returns:
            tuple[np.ndarray[Any, np.dtype[np.signedinteger[Any]]],
            np.ndarray[Any, np.dtype[np.signedinteger[Any]]]]:
            Array indexes.
        """
        return np.where(board == abs_pos)

    def play_game(self):
        """
        Deploy the needed commands and board game state in console.
        """
        print("Welcome to the Snakes and Ladders game! ")
        input("Press enter to start...")
        game_finished = False
        while not game_finished:
            self.print_board()
            input("Press enter to roll the dice...")
            dice_val = self.throw_dice()
            print("You got", dice_val)
            game_finished = self.change_game_state(dice_val)
        print("Congratulations, you have won the game!!!")
