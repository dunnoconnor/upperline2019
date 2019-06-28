import random
from random import randint

class Weapon:
  def __init__(self, name, wDamage, wRange, price):
    self.name = name;
    self.wDamage = wDamage;
    self.wRange = wRange;
    self.price = price;
    
class Armor:
  def __init__(self, name, aRating, price):
    self.name = name;
    self.aRating = aRating;
    self.price = price;
    
class Gear:
  def __init__(self, name, price, description):
    self.name = name;
    self.price = price;
    self.description = description;
