import random


class OrkNameGenerator:
 klinkers = ['a','e','i','o','u']
 medeklinkers = ['g','b','z','k']

 @classmethod
 def get_random_ork_name(cls):
   return random.choice(cls.medeklinkers) + \
   random.choice(cls.klinkers) + \
   random.choice(cls.medeklinkers)
   
for _ in range(10):
 print(OrkNameGenerator.get_random_ork_name())