from wezen import Creature
class Monster(Creature):
    def _init_(self, name, hp = 100, ap = 20):
        self.name = name
        self.hp = hp
        self.ap = ap
        