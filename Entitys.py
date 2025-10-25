from random import randint

class Entity:
    hp = 0
    damage = 0
    armor = 0
    speed = 0
    crit = 0

    def __init__(self, hp, damage, speed, crit, armor=0):
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
    
    def Entity_base(self, a, b, c, d, e):
        hp = self.hp
        damage = self.damage
        crit = self.crit
        armor = self.armor
        hp = a
        damage = b
        crit = randint(c, d)
        armor = e
        return hp, damage, crit, armor


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
        super(Entity).__init__(0, 0, 0, self.crit_damage(0, 0), 0)

    def zombie(self):
        hp, damage, crit, armor = Entity().Entity_base(20, 10, 1, 3, 0)