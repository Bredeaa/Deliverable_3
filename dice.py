# INF201 - Deliverable 3
# Task 2:  Introducing randomness with a Dice class

import random

class Dice:
    """Represents a dice block"""
    def __init__(self, sides: int = 6) -> None:
        """Dice should have a specific number of sides, expect nothing under 2 sides"""
        if sides < 2:
            raise ValueError("No sides under the value 2!")
        self.sides = sides

    def roll(self) -> int:
        """Rolls a random number beetween one and self.sides"""
        rolls = random.randint(1, self.sides)
        return rolls

    def __repr__(self) -> str:
        """Returns string representations of the dice sides"""
        return (f"Dice(sides={self.sides})")

    def __call__(self) -> int:
        """Makes a function that allows the dice object to be called to roll the dice"""
        return self.roll()