from monster import Monster
import OrkNaamGenerator
import colorama

class Room():
     def get_name(self):
            return self.name

    def get_description(self):
        return self.description

    def _init_(self, name, aantalMonsters=3, description):
        self.name=name
        self.aantalMonsters = []
        self.attachedRooms = [] 
        for i in range(aantalMonsters):
            self.monsters.append(Monster(OrkNameGenerator.get_random_ork_name()))
            self.description = description

    def Attach(self, room):
            self.attachedRooms.append(room)
            if not self in room._attachedRooms:
            room.Attach(self)

     def PrintRoomMenu(self):
            init()
        print(Fore.GREEN + self._description + Style.RESET_ALL)

        self.PrintAttachedRooms()
        self.PrintMonsters()

        print("x. Leave game")


        
