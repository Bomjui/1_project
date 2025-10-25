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

    def Weapon_give(self):
        classes = Randomas().Rndm_class()

        if classes == "common":
            return self.for_Event(info_all.specification, info_all.catalog_price, 0, 5, "common", 0)

        elif classes == "uncommon":
            return self.for_Event(info_all.specification, info_all.catalog_price, 0, 5, "uncommon", 1)

        elif classes == "rare":
            return self.for_Event(info_all.specification, info_all.catalog_price, 0, 5, "rare", 2)

        elif classes == "epic":
            return self.for_Event(info_all.specification, info_all.catalog_price, 0, 5, "epic", 3)

        elif classes == "mythical":
            return self.for_Event(info_all.specification, info_all.catalog_price, 0, 5, "mythical", 4)

    def market(self):
        print("Добро пожаловать в магазин")
        print("Снизу вы можете увидеть наш католог")


        for i in info_all.shop_catalog:
            print(i, end=" ")

        choice_catalog = int(input())

        def shop_logic(arr):
            catalog_random = Random_C()
            catalog = []
            prices = []

            for i in range(1, 9):
                print(i, end=" ")
                item, price = arr
                catalog.append(item)
                prices.append(price)
                if i == 8:
                    choice_i = int(input())
                    print(f"Вы точно хотите взять предмет {catalog[choice_i-1]} за {prices[choice_i-1]} монет?")
                    choise_weapon = input("Ответ да/нет?: ")
                    if choise_weapon.lower == "да":
                        return catalog[choice_i-1], prices[choice_i-1]
                    else:
                        print("Тогда иди прочь")

        def items_shop():
            shop_logic(self.Items_give())
    
        if choice_catalog == 1:
            shop_logic(self.Weapon_give())
        elif choice_catalog == 2:
            items_shop(self.Items_give)




Vill = Village()
Vill.market()
