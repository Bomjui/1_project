from random import randint

class Entity:
    hp = 0
    damage = 0
    armor = 0
    speed = 0
    crit = 0

    def __init__(self, hp, damage, speed, crit, armor=None):
        self.hp = hp
        self.damage = damage
        self.speed = speed
        self.crit = crit
        self.armor = armor
    def attack(self, entity):
        if self.armor == 0:
            entity.hp = self.hp - (self.damage + self.crit)
        else:
            entity.hp = self.hp - (self.damage + self.crit) * self.armor

    def crit_damage(self, n, j):
        self.crit = randint(n, j)

class Player(Entity):
    inventory = []
    hunger = 100

    def __init__(self, inventory, hunger):
        super().__init__(100, 1, 2, super(Player).crit_damage(0, 2))
        self.inventory = inventory
        self.hunger = hunger

    def attack(self, entity):
        super(Player).attack(entity)

    def inventory_P(self):
        pass

    def hunger_P(self):
        pass

class Monsters(Entity):

    def __init__(self):
        super(Monsters).__init__(0, 0, 0, 0, 0)
