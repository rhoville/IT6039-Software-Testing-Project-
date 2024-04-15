# File 2 (BowlingGame.py)
# This file contains the implementation of a Bowling Game.

class BowlingGame:
    """
    Represents a game of bowling.

    Attributes:
        rolls (list): A list to store the number of pins knocked down in each roll.
    """

    def __init__(self):
        """
        Initializes a new instance of the BowlingGame class.
        """
        self.rolls = []

    def roll(self, pins):
        """
        Record a roll in the game.

        Args:
            pins (int): The number of pins knocked down in the roll.
        """
        self.rolls.append(pins)

    def score(self):
        """
        Calculate the total score of the game.

        Returns:
            int: The total score of the game.
        """
        result = 0
        rollIndex = 0
        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex += 1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex += 2
            else:
                result += self.frameScore(rollIndex)
                rollIndex += 2
        return result

    def isStrike(self, rollIndex):
        """
        Check if a roll is a strike.

        Args:
            rollIndex (int): The index of the roll to check.

        Returns:
            bool: True if the roll is a strike, False otherwise.
        """
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        """
        Check if a frame is a spare.

        Args:
            rollIndex (int): The index of the first roll in the frame.

        Returns:
            bool: True if the frame is a spare, False otherwise.
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10

    def strikeScore(self, rollIndex):
        """
        Calculate the score for a strike frame.

        Args:
            rollIndex (int): The index of the roll containing the strike.

        Returns:
            int: The score for the strike frame.
        """
        return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

    def spareScore(self, rollIndex):
        """
        Calculate the score for a spare frame.

        Args:
            rollIndex (int): The index of the first roll in the spare frame.

        Returns:
            int: The score for the spare frame.
        """
        return 10 + self.rolls[rollIndex + 2]

    def frameScore(self, rollIndex):
        """
        Calculate the score for a normal frame.

        Args:
            rollIndex (int): The index of the first roll in the frame.

        Returns:
            int: The score for the frame.
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
