import info_all
from Randoma import Random_C

class Village:
    shop = False
    the_forge = False
    hotel = False
    def __init__(self, shop=False, the_force=False, hotel=False):
        self.shop = shop
        self.the_forge = the_force
        self.hotel = hotel


    def outline_of_the_village(self, a):
        print(f"Из далека виднеется силует {a}")
        self.village_in()

    def village_in(self):
        print("Вы прибыли в деревню")
        if self.shop == False and self.the_forge == False and self.hotel == False:
            print("А деревня маловата тут ловить нечего")
        else:
            if self.shop == True:
                pass
            elif self.the_forge == True:
                pass
            else:
                pass

    def market(self):
        print("Добро пожаловать в магазин")
        print("Снизу вы можете увидеть наш католог")
        for i in info_all.shop_catalog:
            print(i, end=" ")
        choice_catalog = int(input())
        if choice_catalog == 1:
            catalog_random = Random_C()
            a = []
            for i in range(8):
                a.append(catalog_random.vilage())
Vill = Village()
Vill.market()