# INF201 - Deliverable 3
# Task 4: Mage class

from characters import Character


class Mage(Character):
    """Represents a mage that uses mana for magic attacks"""

    def __init__(
        self, name, hp_max=100, damage=10,weapon=None, mana=30, mana_max=30):
        """Initialise the Mage"""
        super().__init__(name, hp_max, damage, weapon)
        self.mana = mana
        self.mana_max = mana_max

    def attack(self, target):
        """Uses magic if enough mana, otherwise normal attack"""

        if self.mana >= 10:
            self.mana -= 10  # Magic attack costs 10 mana
            target.take_damage(self.damage * 2)  # Double base damage

        else:
            super().attack(target)  # Normal attack with weapon if equipped
            self.mana = min(self.mana + 5, self.mana_max)  # Restore mana
