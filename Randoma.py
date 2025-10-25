from random import randint
import Items
import info_all

class Randomas:
    classes = info_all.classes_1
    def Rndm(self):
        a_rn = randint(1, 100)
        if a_rn <= 65:
            print("No")
            return "No"
        elif a_rn > 65 and a_rn <= 75:
            print("Item")
            return Random_I().Rndm_items()
        elif a_rn > 75 and a_rn <= 95:
            print("Entity")
            return Random_E().Rndm_Entity()
        else:
            print("City")
            return Random_C().Rndm_City()

    def Rndm_class(self):
        a_rn = randint(1, 1000)
        if a_rn == 1:
            return "secret"
        elif a_rn > 1 and a_rn <= 15:
            return "godly"
        elif a_rn > 15 and a_rn <= 40:
            return "legendary"
        elif a_rn > 40 and a_rn <= 80:
            return "mythical"
        elif a_rn > 80 and a_rn <= 230:
            return "epic"
        elif a_rn > 230 and a_rn <= 380:
            return "rare"
        elif a_rn > 380 and a_rn <= 530:
            return "uncommon"
        else:
            return "common"

class Random_C:
    classes = Randomas().Rndm_class()
    def Rndm_City(self):
        a_rn = randint(1, 1000)
        if a_rn <= 50:
            print("City")
            return "city"
        elif a_rn > 50 and a_rn <= 400:
            print("vilage")
            return ("vilage")
        elif a_rn > 400 and a_rn <= 999:
            print("ruins")
            return ("ruins")
        else:
            return "home"

    def city(self):
        pass

    def vilage(self):
        pass

    def ruins(self):
        pass

    def home(self):
        pass

class Random_E:
    def Rndm_Entity(self):
        a_rn = randint(1, 100)
        if a_rn <= 35:
            print("nps")
            return "nps"
        else:
            print("Monsters")
            return ("monsters")

class Random_I:
    def Rndm_items(self):
            a_rn = randint(1, 100)
            if a_rn <= 30:
                print("more_weapon")
                return self.Rndm_mw()
            elif a_rn > 30 and a_rn <= 60:
                print("Item")
                return self.Rndm_Item()
            elif a_rn > 60 and a_rn <= 80:
                print("Entity")
                return self.rndm_food()
            elif a_rn > 80 and a_rn <= 95:
                print("City")
                return self.money()
            else:
                print("weapon")
                return self.weapon()

    def Rndm_mw(self):
        a_rn = randint(1, 100)
        if a_rn <= 25:
            print("stick")
            return "stick"
        elif a_rn > 25 and a_rn <= 50:
            print("rock")
            return "rock"
        elif a_rn > 50 and a_rn <= 75:
            print("bone")
            return "bone"
        else:
            print("flower")
            return "flower"

    def Rndm_Item_if_else(self, arr, a, b, c, d, e, f):
        a_rn = randint(1, 100)
        if a_rn <= a:
            print(arr[0])
            return arr[0]
        elif a_rn > a and a_rn <= b:
            print(arr[1])
            return arr[1]
        elif a_rn > b and a_rn <= c:
            print(arr[2])
            return arr[2]
        elif a_rn > c and a_rn <= d:
            print(arr[3])
            return arr[3]
        elif a_rn > d and a_rn <= e:
            print(arr[4])
            return arr[4]
        elif a_rn > e and a_rn <= f:
            print(arr[5])
            return arr[5]
        else:
            print(arr[6])
            return arr[6]

    def Rndm_Item(self):
        classes = Randomas().Rndm_class()
        a_rn = randint(1, 100)

        if classes == "secret":
            self.Rndm_Item_if_else(info_all.secret_items, 10, 20, 30 , 55, 80, 90)
        elif classes == "godly":
            self.Rndm_Item_if_else(info_all.godly_items, 1, 10, 30, 45, 60, 85)
        elif classes == "legendary":
            self.Rndm_Item_if_else(info_all.legendary_items, 10, 25, 40, 60, 70, 85)
        elif classes == "mythical":
            self.Rndm_Item_if_else(info_all.mythical_items, 20, 30, 55, 60, 70, 85)
        elif classes == "epic":
            self.Rndm_Item_if_else(info_all.epic_items, 15, 30, 45, 60, 70, 80)
        elif classes == "rare":
            self.Rndm_Item_if_else(info_all.rare_items, 20, 30, 45, 50, 60, 80)
        elif classes == "uncommon":
            self.Rndm_Item_if_else(info_all.uncommon_items, 5, 10, 25, 55, 65, 80)
        else:
            self.Rndm_Item_if_else(info_all.common_items, 15, 30, 45, 65, 80, 90)


    def rndm_food(self):
        a_rn = randint(1, 100)
        def Food_1():
            if a_rn == 1:
                return secret_food()
            else:
                return food_Random()

        def food_Random():
            a_rn = randint(1, 100)
            a_rn_1 = randint(0, 9)
            if a_rn <= 50:
                return info_all.foods_list_1[a_rn_1]
            elif a_rn > 50 and a_rn <= 80:
                return info_all.foods_list_2[a_rn_1]
            elif a_rn > 80 and a_rn <= 95:
                return info_all.foods_list_3[a_rn_1]
            else:
                return info_all.foods_list_4[a_rn_1]

        def secret_food():
            a_rn = randint(1, 3)
            return info_all.secret_items[a_rn]

    def money(self):
        a_rn = randint(1, 100)

        if a_rn <= 80:
            print("coins")
            return self.Rndm_Item_if_else(info_all.coins, 35, 55, 70, 80, 89, 96)

        else:
            print("paper money")
            return self.Rndm_Item_if_else(info_all.money_paper, 35, 55, 70, 80, 89, 96)

    def weapon(self):
        classes = Randomas().Rndm_class()

        def for_Event(arr, n, j, d, super_class=False):
            a_rn = randint(n, j)
            if super_class == False:
                for i in arr.keys():
                    if i == d:
                        a = arr[d]
                        print(f"Редкость: /{d.title()}/-->", a[a_rn])
                        return a[a_rn]
            else:
                b = []
                a = arr.values()
                for i in a:
                    b.append(i)
                print(f"Редкость: |{d.title()}|-->", b[a_rn])
                return b[a_rn]

        def weapon_name():
            if classes == "common":
                for_Event(info_all.specification, 0, 5, "common")

            elif classes == "uncommon":
                for_Event(info_all.specification, 0, 5, "uncommon")

            elif classes == "rare":
                for_Event(info_all.specification, 0, 5, "rare")

            elif classes == "epic":
                for_Event(info_all.specification, 0, 5, "epic")

            elif classes == "mythical":
                for_Event(info_all.specification, 0, 5, "mythical")

            elif classes == "legendary":
                print("Похоже вам повезло...")
                for_Event(info_all.legendary_spec, 0, 17, "legendary", super_class=True)

            elif classes == "godly":
                print("Это будет божественно...")
                for_Event(info_all.godly_spec, 0, 17, "godly", super_class=True)

            else:
                print("Невозможно.....")
                print("Невозможно....")
                print("Невозможно...")
                print("Невозможно..")
                print("Невозможно.")
                for_Event(info_all.secret_spec, 0, 6, "SECRET", super_class=True)


        weapon_name()
