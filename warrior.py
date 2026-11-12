# INF201 - Deliverable 3
# Task 4: Warrior class

from characters import Character


class Warrior(Character):
    """Represents a warrior with armor to reduce damage"""

    def __init__(self, name, hp_max=100, damage=10, weapon=None, armor=5):
        """Initialise the Warrior"""
        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor

    def take_damage(self, damage):
        """Reduces incoming damage using armor"""
        damage = max(0, damage - self.armor)  # Damage cannot be negative
        super().take_damage(damage)  # Uses Character's method
