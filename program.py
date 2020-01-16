from Held import Hero
import Monster
import OrkNaamGenerator
import Wezen

hero = Hero("Immahero", 200, 80)

Hall = Room("hall", description="A very narrow hallway...")
kitchen = Room("Kitchen",15, "It smells like something died in here...")
office = Room("office", 10, "So muchù work todo... and monsters to kill...")
frontgarden = Room("frontgarden",5,"...")
backgarden = Room("backgarden",6,"...")
pool = Room("pool",100,"This pool is infested with monsters!")

frontgarden.attach(Hall)
hall.attach(kitchen)
hall.attach(office)
hall.attach(backgarden)
backgarden.attach(pool)
frontgarden.enter(hero)
