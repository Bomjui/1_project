from random import randint
import info_all

class Items:
    classes = info_all.classes_1
    specifications = []

    def __init__(self, classes, specification):
        self.classes = classes
        self.specifications = specification


class Weapon(Items):
    cooldown = {}

    def __init__(self, cooldown=0):
        super().__init__(self.classes, self.specifications)
        self.type_w = info_all.type_weapon
        self.spec = info_all.specification
        self.legendary = info_all.legendary_spec
        self.godly = info_all.godly_spec
        self.secret = info_all.secret_spec
        self.cooldown = cooldown

    def class_damage(self):
        damage_n = 0
        for i in self.classes[1:7]:
            if i == "uncommon":
                damage_n += randint(2, 4)
                return damage_n
            elif i == "rare":
                damage_n += randint(5, 8)
                return damage_n
            elif i == "epic":
                damage_n += randint(9, 12)
                return damage_n
            elif i == "mythical":
                damage_n += randint(14, 20)
                return damage_n
            elif i == "legendary":
                damage_n += randint(25, 35)
                return damage_n
            elif i == "godly":
                damage_n += randint(67, 101)
                return damage_n

    def Specifications(self, n=0, j=0, g=0):

        if self.class_damage() <= 35:
            rand = randint(0, 2)
            spec_k = self.legendary.keys()[n:j]
            spec = spec_k[rand - 1:rand]
            return spec
        elif self.class_damage() <= 101:
            rand = randint(0, 2)
            spec_k = self.godly.keys()[n:j]
            spec = spec_k[rand - 1:rand]
            return spec

    def c_u(self, n):
        for i in range(0, 5):
            if self.classes[i] == self.spec.keys()[i - 1:i]:
                for j in range(0, 6):
                    if self.spec.values()[j - 1:j] == n:
                        spec_k = self.spec.values()[j - 1:j]
                        return spec_k

    def Bow(self, attack_f=False, characteristic=False):
        if attack_f == True:
            damage_w = 2 + self.class_damage()
            return damage_w
        if characteristic == True:
            print(self.c_u(0))

    def Sword(self, attack_f=False, characteristic=False):
        if attack_f == True:
            damage_w = 3 + self.class_damage()
            return damage_w
        if characteristic == True:
            print(self.c_u(1))

    def Shield(self, attack_f=False, characteristic=False):
        if attack_f == True:
            s_w = randint(1, 3) + self.class_damage()
            return s_w
        if characteristic == True:
            print(self.c_u(2))

    def Spear(self, attack_f=False, characteristic=False):
        if attack_f == True:
            damage_w = 3.5 + self.class_damage()
            return damage_w
        if characteristic == True:
            print(self.c_u(3))

    def Staff(self, attack_f=False, characteristic=False):
        if attack_f == True:
            damage_w = 4 + self.class_damage()
            return damage_w
        if characteristic == True:
            print(self.c_u(4))

    def Hammer(self, attack_f=False, characteristic=False):
        if attack_f == True:
            damage_w = 6 + self.class_damage()
            return damage_w
        if characteristic == True:
            print(self.c_u(5))