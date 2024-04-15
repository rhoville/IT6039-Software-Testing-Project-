# File 1 (Test.py)
# This file has information about test cases which you need to test.

import unittest
import BowlingGame


class TestBowlingGame(unittest.TestCase):
    """
    A test suite for the BowlinGame class.
    """

    def setUp(self):
        """
        Set up the test fixture.
        """
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        """
        Test a gutter game where all rolls are 0.
        """
        for i in range(0, 20):
            self.game.rolls(0)
        assert self.game.score() == 0

    def testAllOnes(self):
        """
        Test a game where all rolls knock down one pin.
        """
        self.rollMany(1, 20)
        assert self.game.score() == 20

    def testOneSpare(self):
        """
        Test a game with one spare.
        """
        self.game.rolls(5)
        self.game.rolls(5)
        self.game.rolls(3)
        self.rollMany(0, 17)
        assert self.game.score() == 16

    def testOneStrike(self):
        """
        Test a game with one strike.
        """
        self.game.rolls(10)
        self.game.rolls(4)
        self.game.rolls(3)
        self.rollMany(0, 16)
        assert self.game.score() == 24

    def testPerfectGame(self):
        """
        Test a perfect game with all strikes.
        """
        self.rollMany(10, 12)
        assert self.game.score() == 300

    def testMultipleSpares(self):
        """
        Test a game with multiple spares.
        """
        self.rollMany(5, 21)
        assert self.game.score() == 150

    def rollMany(self, pins, rolls):
        """
        Roll a specific number of pins for a specific number of rolls.

        Args:
            pins (int): The number of pins to roll.
            rolls (int): The number of rolls.
        """
        for i in range(rolls):
            self.game.rolls(pins)
