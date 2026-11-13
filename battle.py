# INF201 - Deliverable 3
# Task 5: Running battles

from characters import Character


class Battle:
    """Represents a battle between two characters in the RPG"""

    def __init__(self, hero: Character, enemy: Character):
        """Initialise the Battle"""
        self.hero = hero
        self.enemy = enemy

    def play_round(self):
        """Hero attacks first, then enemy if still alive"""

        before = self.enemy.hp  # Save enemy HP before attack
        self.hero.attack(self.enemy)

        damage = before - self.enemy.hp  # Calculate HP lost
        print(f"{self.hero.name} attacks {self.enemy.name}: {damage} damage")

        if self.enemy.is_alive:
            before = self.hero.hp  # Save hero HP before attack
            self.enemy.attack(self.hero)

            damage = before - self.hero.hp
            print(f"{self.enemy.name} attacks {self.hero.name}: {damage} damage")

    def simulate_battle(self):
        """Runs battle rounds until one character reaches 0 HP"""

        round_number = 1

        while self.hero.is_alive and self.enemy.is_alive:

            print(f"\n--- Round {round_number} ---")

            self.play_round()

            # Show remaining HP
            print(f"{self.hero.name}: {self.hero.hp} HP")
            print(f"{self.enemy.name}: {self.enemy.hp} HP")

            round_number += 1

        if self.hero.is_alive:
            print(f"\nWinner: {self.hero.name}")
        else:
            print(f"\nWinner: {self.enemy.name}")
