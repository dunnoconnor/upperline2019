import random
from random import randint

class Hero:
  
  def __init__(self):
    self.name = "NONE";
    self.job = "NONE";
    self.level = 1;
    self.strength = random.randint(1, 3);
    self.speed = random.randint(1, 3);
    self.max_health = random.randint(6, 12);
    self.health = self.max_health;
  
  def resetHero(self):
    self.name = "NONE";
    self.job = "NONE";
    self.level = 1;
    self.strength = random.randint(1, 3);
    self.speed = random.randint(1, 3);
    self.max_health = random.randint(6, 12);
    self.health = self.max_health;
  
  def setName(self,name):
    self.name = name;
  
  def setJob(self,job):
    self.job = job;
  
  def heal(self):
    self.health = self.max_health;
  
  def jobStats(self):
    if self.job == "FIGHTER":
      self.strength = self.strength + 2;
    elif self.job == "THIEF":
      self.speed = self.speed + 2;
    
  def levelUp(self, hero, room):
    if self.level == 1 and room.level > 4:
      self.level = 2;
      self.jobStats();
    elif self.level == 2 and room.level > 7:
      self.level = 3;
      self.jobStats();