import info_all
from random import randint
from Randoma import Random_C, Randomas

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

    def for_Event(self, arr, arr_2, n, j, d, price_index):
        a_rn = randint(n, j)
        for i in arr.keys():
            if i == d:
                a = arr[d]
                print(f"--> Предмет: {a[a_rn]} | Цена: {arr_2[price_index]} монеты")
                return a[a_rn], arr_2[price_index]

    def Item_give(self):
        classes = Randomas().Rndm_class()

        if classes == "common":
            a = self.for_Event(info_all.specification, info_all.catalog_price, 0, 5, "common", 0)
            return a

        elif classes == "uncommon":
            a = self.for_Event(info_all.specification, info_all.catalog_price, 0, 5, "uncommon", 1)
            return a

        elif classes == "rare":
            a = self.for_Event(info_all.specification, info_all.catalog_price, 0, 5, "rare", 2)
            return a

        elif classes == "epic":
            a = self.for_Event(info_all.specification, info_all.catalog_price, 0, 5, "epic", 3)
            return a

        elif classes == "mythical":
            a = self.for_Event(info_all.specification, info_all.catalog_price, 0, 5, "mythical", 4)
            return a

    def market(self):
        print("Добро пожаловать в магазин")
        print("Снизу вы можете увидеть наш католог")


        for i in info_all.shop_catalog:
            print(i, end=" ")
        choice_catalog = int(input())
        if choice_catalog == 1:
            catalog_random = Random_C()
            catalog = []


            for i in range(1, 9):
                print(i, end=" ")
                item, price = self.Item_give()
                catalog.append(item)
                if i == 8:
                    choice_i = int(input())
                    print(f"Предмет {catalog[choice_i + 1]} за {price}")




Vill = Village()
Vill.market()