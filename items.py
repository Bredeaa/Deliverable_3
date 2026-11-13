# INF201 - Deliverable 3
# Task 3: Create items

from dice import Dice


class Weapon:
    """Represents a weapon in the RPG"""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """Initialise the Weapon"""
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Rolls the weapon's dice to determine damage"""
        return self.damage_dice.roll()