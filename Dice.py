import random

class Dice():

   def __init__(self, sides, numDice):
      self.sides = sides
      self.numDice = numDice

   def roll(self):
      min = 1
      max = self.sides
      totalRollValue = 0
      allRolls = []
      for i in range(self.numDice):
         rollValue = random.randint(min, max)
         allRolls.append(rollValue)
         totalRollValue += rollValue
      print(allRolls)
      return totalRollValue


'''
d1 = Dice(6, 10)
d1.roll() # will only output the print() statement
print(d1.roll()) # will output the print() statement and then the return statement
'''