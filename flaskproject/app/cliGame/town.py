import random
from random import randint
from app.cliGame import arsenal

class Town:
  
  hands = arsenal.Weapon("HANDS",1,0,0);
  staff = arsenal.Weapon("STAFF",1,2,1);
  dagger = arsenal.Weapon("DAGGER",2,0,1);
  axe = arsenal.Weapon("AXE",3,1,3);
  spear = arsenal.Weapon("SPEAR",3,2,3);
  bow = arsenal.Weapon("BOW",2,3,4);
  sword = arsenal.Weapon("SWORD",4,1,6);
  noArmor = arsenal.Armor("NONE",0,0);
  leather = arsenal.Armor("LEATHER",1,3);
  chain = arsenal.Armor("CHAIN",2,6);
  plate = arsenal.Armor("PLATE",3,9);
  torch = arsenal.Gear("TORCH",1,"Each trip into the wild uses one torch");
  ration = arsenal.Gear("RATION",1,"Rations can be used to reself health in camp");
  shield = arsenal.Gear("SHIELD",5,"A shield grants extra armor");
  helmet = arsenal.Gear("HELMET",3,"A helmet grants extra armor");
  cloak = arsenal.Gear("CLOAK",3,"A cloak makes you better at sneaking");
  tavern = arsenal.Gear("TAVERN",40,"A way to make a living without adventuring");
  
  weaponList = [staff, dagger, axe, spear, bow, sword];
  armorList = [leather, chain, plate];
  gearList = [shield, helmet, cloak];
  
  def __init__(self):
    self.torch = Town.torch;
    self.ration = Town.ration;
    self.weapon = Town.weaponList[random.randint(0,len(Town.weaponList)-1)];
    self.armor = Town.armorList[random.randint(0,len(Town.armorList)-1)];
    self.gear = Town.gearList[random.randint(0,len(Town.gearList)-1)];
    self.tavern = Town.tavern;
    self.storeWeapon = (self.weapon.name + ": " + str(self.weapon.price) + " Gold");
    self.storeArmor = (self.armor.name + " ARMOR: " + str(self.armor.price) + " Gold");
    self.storeGear = ("GEAR - " + self.gear.name + ": " + str(self.gear.price) + " Gold" );
    
  def rollTown(self):
    self.torch = Town.torch;
    self.ration = Town.ration;
    self.weapon = Town.weaponList[random.randint(0,len(Town.weaponList)-1)];
    self.armor = Town.armorList[random.randint(0,len(Town.armorList)-1)];
    self.gear = Town.gearList[random.randint(0,len(Town.gearList)-1)];
    self.tavern = Town.tavern;
    self.storeWeapon = (self.weapon.name + ": " + str(self.weapon.price) + " Gold");
    self.storeArmor = (self.armor.name + " ARMOR: " + str(self.armor.price) + " Gold");
    self.storeGear = ("GEAR - " + self.gear.name + ": " + str(self.gear.price) + " Gold" );