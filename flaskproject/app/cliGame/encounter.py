import random
from random import randint

class Conflict:
  
  def __init__(self):
    self.closeRange = False;
    self.victory = False;
    self.defeat = False;
    self.escape = False;
    self.resultA = "";
    self.resultB = "";
    self.resultC = "";
    self.counterA = "";
    self.counterB = "";
    self.counterC = "";
  
  def resetConflict(self):
    self.closeRange = False;
    self.victory = False;
    self.defeat = False;
    self.escape = False;
    self.resultA = "";
    self.resultB = "";
    self.resultC = "";
    self.counterA = "";
    self.counterB = "";
    self.counterC = "";
  
  def chooseAction(self, hero, inv, target, choice):
    if (choice == "ATTACK"):
      self.attack(hero, inv, target);
    elif (choice == "MANEUVER"):
      self.maneuver(hero, inv, target);
    else:
      self.sneak(hero, inv, target);
      
  def chooseNextAction(self, hero, inv, target, choice):
    if (choice == "ATTACK"):
      self.attack(hero, inv, target);
    elif (choice == "MANEUVER"):
      self.maneuver(hero, inv, target);
    else:
      self.flee(hero, inv, target);

    
  def attack(self, hero, inv, target):
    if (self.closeRange == False):
      self.resultA = (hero.name + " attacks the " + target.title + " from afar!");
      if (inv.weaponRange > target.range):
        self.resultB = (hero.name + " outranges the " + target.title + ".  The attack is more effective.");
        damage = hero.strength + inv.weaponDamage + random.randint(1,2);
      elif (inv.weaponRange < target.range):
        self.resultB = ("The  " + target.title + " outranges " + hero.name + ".  The attack is less effective.");
        damage = hero.strength + inv.weaponDamage - random.randint(1,2);
      else:
        self.resultA = (hero.name + " and the " + target.title + " circle each other.  The attack goes through normally.")
        damage = hero.strength + inv.weaponDamage;
    else:
      self.resultA = (hero.name + " attacks the " + target.title + " up close!");
      if (inv.weaponRange < target.range):
        self.resultB = (hero.name + " gets through the " + target.title + "'s defenses.  The attack is more effective.");
        damage = hero.strength + inv.weaponDamage + random.randint(1,2);
      elif (inv.weaponRange > target.range):
        self.resultB = ("The  " + target.title + " keeps " + hero.name + " back.  The attack is less effective.");
        damage = hero.strength + inv.weaponDamage - random.randint(1,2);
      else:
        self.resultB = (hero.name + " and the " + target.title + " are close enough to grapple.  The attack goes through normally.")
        damage = hero.strength + inv.weaponDamage;
    damage -= target.armor;
    if damage < 0:
      damage = 0;
    target.health -= damage
    self.resultC = ("The " + target.title + " now has " + str(target.health) + " health remaining.\n");
    if target.health<1:
      self.victory = True;
    if self.victory == False:
      self.counterattack(hero, inv, target);
    
  def counterattack(self, hero, inv, target):
    if (self.closeRange == False):
      self.counterA = ("The " + target.title + " counterattacks from afar!");
      if (inv.weaponRange > target.range):
        self.counterB = (hero.name + " outranges the " + target.title + ".  The counterattack is less effective.");
        mDamage = target.damage - random.randint(1,2);
      elif (inv.weaponRange < target.range):
        self.counterB = ("The  " + target.title + " outranges " + hero.name + ".  The counterattack is more effective.");
        mDamage = target.damage + random.randint(1,2);
      else:
        self.counterB = (hero.name + " and the " + target.title + " circle each other.  The counterattack goes through normally.")
        mDamage = target.damage;
    else:
      self.counterA = ("The " + target.title + " counterattacks up close!");
      if (inv.weaponRange > target.range):
        self.counterB = ("The " + target.title + " gets through " + hero.name + "'s defenses.  The counterattack is more effective.");
        mDamage = target.damage + random.randint(1,2);
      elif (inv.weaponRange > target.range):
        self.counterB = (hero.name + " keeps the " + target.title + " back.  The counterattack is less effective.");
        mDamage = target.damage - random.randint(1,2);
      else:
        self.counterB = (hero.name + " and the " + target.title + " are close enough to grapple.  The counterattack goes through normally.")
        mDamage = target.damage;
    mDamage -= inv.armorRating;
    if mDamage < 0:
      mDamage = 0;
    hero.health -= mDamage
    self.counterC = (hero.name + " now has " + str(hero.health) + " / " + str(hero.max_health) + " health remaining.\n");
    if hero.health<1:
      self.defeat = True;
  
  def maneuver(self, hero, inv, target):
    if (self.closeRange == False):
      self.closeRange = True;
      self.resultA = (hero.name + " gets in close.");
    else:
      self.closeRange = False;
      self.resultA = (hero.name + " steps back, ready to attack from range.");
    self.counterattack(hero, inv, target);
  
  def flee(self, hero, inv, target):
    self.resultA = (hero.name + " attempts to flee.");
    huntRating = target.range + (target.armor/2) + random.randint(0,2);
    if (hero.speed + inv.speedBonus) >= huntRating:
      self.escape = True;
    else:
      self.counterattack(hero, inv, target);
    
  def sneak(self, hero, inv, target):
    self.resultA = (hero.name + " attempts to sneak past.");
    huntRating = target.range + target.armor + random.randint(0,2);
    sneakRating = hero.speed + inv.stealthiness;
    if sneakRating > huntRating:
      self.escape = True;
    else:
      self.counterattack(hero, inv, target);
    
    