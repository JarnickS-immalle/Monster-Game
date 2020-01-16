import random
import colorama 
class Creature:
    def _init_(self, name, hp = 100, ap = 20):
        self.name = name
        self.hp = hp
        self.ap = ap


    def Attack(self, c):
        damage = random.randint(0, c.ap + 1)
        c.hp -= damage
        if (c.hp <= 0):
            colorama.init()
            print(f"{colorama.Fore.RED} {self.name} attacks {c.name} and does {damage}. {c.name} dies.{colorama.Style.RESET_ALL}")
            return True
        else:
            print(f"{self.name} attacks {c.name} and does {damage}.")
            return False





