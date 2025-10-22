from Randoma import Randomas, Random_I, Random_C, Random_E
import Location

class Game:
    def Game_main(self):
        print("\n_______", "\t______")
        print("|start|", "\t|exit|")
        print("^^^^^^^", "\t^^^^^^")
        print("Для старта напишите 1: ", "\nА для выхода 2:")
        a = int(input())
        if a == 1:
            self.Story_start()
        else:
            print("Ok")
    def Story_start(self):
        print("Давным давно был путник что потерялся...")
        print("Он не знал что делать...")
        print("Может вы поможете ему вернутся и не умереть в этом суровом мире?")
        print("Приготовтесь это будет интерестно...")

    def Story_2(self):
        print("Walk")


game = Game()
game.Game_main()
