from Wezen import Creature
class Hero(Creature):
    def _init_(self, name, hp = 1000, ap = 30):
        self.name = name
        self.hp = hp
        self.ap = ap