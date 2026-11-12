# INF201 - Deliverable 3
# Task 1: Update the Character class

class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon=None) -> None:
        """
        Initialise the Character
        
        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
            weapon (Weapon): The weapon the character wields (default = None)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def take_damage(self, damage: int) -> None:
        """Character object(self) takes damage"""
        self._hp -= damage
        self._hp = max(self._hp, 0)  # Self hp cannot end up lower than 0

    def attack(self, target) -> None:
        """Attack and deal damage to target character using function(take_damage)"""
        if self.weapon is not None:
            target.take_damage(self.weapon.roll_damage())
        else:
            target.take_damage(self.damage)

    def heal(self, healing_amount: int) -> None:
        """Character heals themselves"""
        self._hp += healing_amount
        self._hp = min(self._hp, self.hp_max)  # Hp never goes over hp_max

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    @property 
    def is_alive(self) -> bool:
        """A Public read-only property that returns "True" if _hp > 0 or False if it isn't"""
        if self._hp > 0:
            return True
        else:
            return False