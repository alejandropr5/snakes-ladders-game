from typing import Optional, Dict
import numpy as np


class SnakesAndLadders:
    def __init__(
        self,
        snakes: Dict[int, int] = {
            14: 4,
            19: 8,
            22: 20,
            24: 16
        },
        ladders: Dict[int, int] = {
            3: 11,
            6: 17,
            9: 18,
            10: 12
        }
    ) -> None:
        """Create a new SnakesAndLadders object.

        Args:
            snakes (dict[int, int]): Map for board snakes, where keys
                are the snakes head and values the snakes tail. Defaults
                to { 14: 4, 19: 8, 22: 20, 24: 16 }.
            ladders (dict[int, int]): Map for board ladders, where keys
                are the ladders start and values the ladders end.
                Defaults to { 3: 11, 6: 17, 9: 18, 10: 12 }.
        """
        self.__snakes = snakes
        self.__ladders = ladders
        self.__board = np.array([[21, 22, 23, 24, 25],
                                 [20, 19, 18, 17, 16],
                                 [11, 12, 13, 14, 15],
                                 [10, 9, 8, 7, 6],
                                 [1, 2, 3, 4, 5]])

        self.__board_display = np.full([5, 5], "  ", dtype="<U10")
        for i, (key, value) in enumerate(self.__snakes.items()):
            label = f"S{i + 1}"
            self.__board_display[np.where(self.__board == key)] = label
            self.__board_display[np.where(self.__board == value)] = label
        for i, (key, value) in enumerate(self.__ladders.items()):
            label = f"L{i + 1}"
            self.__board_display[np.where(self.__board == key)] = label
            self.__board_display[np.where(self.__board == value)] = label

        self.__pos = 0

    @property
    def pos(self) -> int:
        return self.__pos

    @pos.setter
    def pos(self, pos: Optional[int]) -> None:
        raise AttributeError("Invalid variable assignation. "
                             "Use move() method instead.")

    @staticmethod
    def roll_dice() -> int:
        """Simulate rolling a dice, returning a random integer between
        1 and 6.
        """
        return np.random.randint(1, 7)

    def move(self, movement: int) -> str:
        """Change the player's position given a number of moves, taking
            into account whether he falls into a snake or ladder.

        Args:
            movement (int): Number of positions to move.

        Returns:
            str: Message with current position. Indicating whether the
                player fell into a snake or ladder.
        """
        self.__pos += movement
        message = f"You are in position {self.pos}"
        if self.pos <= 25:
            if self.pos in self.__snakes:
                new_pos = self.__snakes[self.pos]
                message = (f"Oh no! You landed on square {self.pos} but fell"
                           f" by a snake to square {new_pos}.")
                self.__pos = new_pos
            if self.pos in self.__ladders:
                new_pos = self.__ladders[self.pos]
                message = (f"You landed on square {self.pos} but took a "
                           f"shortcut to square {new_pos}!")
                self.__pos = new_pos

            return message
        return ""

    def __str__(self) -> str:  # pragma: no cover
        """Return the current state of the board as a string."""
        header = ("This is your current board:\n")
        y_margin = "+------"*5 + "+\n"

        board = header + y_margin

        for i in range(self.__board.shape[0]):
            for j in range(self.__board.shape[1]):
                board += f"|    {self.__board[i, j]:2d}"
            board += "|\n"

            for j in range(self.__board.shape[1]):
                piece = "  "
                if self.__board[i, j] == self.pos:
                    piece = "XX"
                board += f"|  {piece}  "
            board += "|\n"

            for j in range(self.__board.shape[1]):
                board += f"|{self.__board_display[i, j]}    "
            board += "|\n"

            board += y_margin

        return board

    def play_game(self) -> None:  # pragma: no cover
        """Run the game via console."""
        print("Welcome to the Snakes and Ladders game! ")
        input("Press enter to start...")

        while self.pos <= 25:
            print(self)
            input("Press enter to roll the dice...")
            dice_val = self.roll_dice()
            print("You got", dice_val)
            print(self.move(dice_val))
        print("Congratulations, you have won the game!!!")
