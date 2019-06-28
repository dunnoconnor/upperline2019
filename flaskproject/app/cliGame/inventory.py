import random
from random import randint
from app.cliGame import arsenal

class Inventory:
  
  spells = ["Mage Armor", "Cloak of Shadow", "Fireball", "Levitation"];
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
  ration = arsenal.Gear("RATION",1,"Rations can be used to restore health in camp");
  shield = arsenal.Gear("SHIELD",5,"A shield grants extra armor");
  helmet = arsenal.Gear("HELMET",3,"A helmet grants extra armor");
  cloak = arsenal.Gear("CLOAK",3,"A cloak makes you better at sneaking");
  
  def __init__(self):
    self.gold = 0;
    self.torches = 4;
    self.rations = 2;
    self.weapon = Inventory.hands;
    self.baseDamage = 0;
    self.weaponDamage = 1;
    self.weaponRange = 0;
    self.baseArmor = 0;
    self.armor = Inventory.noArmor;
    self.helmet = False;
    self.shield = False;
    self.armorRating = 0;
    self.cloak = False;
    self.coreStealth = 3;
    self.stealthiness = self.coreStealth;
    self.speedBonus = 0;
    self.knownSpell = "NONE";
    self.spellText = "";
    self.rationText = "eats a ration and recovers health.";
    
  def checkItemEffects(self):
    self.weaponDamage = self.weapon.wDamage;
    self.weaponRange = self.weapon.wRange;
    self.stealthiness = (self.coreStealth - self.armor.aRating);
    self.armorRating = (self.baseArmor + self.armor.aRating);
    if self.helmet == True:
      self.armorRating += 1;
      self.stealthiness -= 1;
    if self.shield == True:
      self.armorRating += 2;
      self.stealthiness -=2;
    if self.cloak == True:
      self.stealthiness +=2;

  def jobItems(self, job):
    if job == "WIZARD":
      self.weapon = Inventory.staff;
      self.knownSpell = Inventory.spells[random.randint(0,(len(Inventory.spells)-1))];
    elif job == "THIEF":
      self.weapon = Inventory.dagger;
      self.coreStealth += 1;
    else:
      self.weapon = Inventory.axe;
      self.helmet = True;
    self.checkItemEffects();
    
  def burnTorch(self):
    self.torches -= 1;
    
  def eatRation(self):
    if self.rations > 0:
      self.rationText = "eats a ration and recovers health."
      self.rations -= 1;
    else:
      self.rationText = "is out of rations!"
  
  def buyTorch(self):
    self.gold -= Inventory.torch.price;
    self.torches += 1;
    
  def buyRation(self):
    self.gold -= Inventory.ration.price;
    self.rations += 1;
    
  def buyGear(self, item):
    self.gold -= item.price;
    if item == Inventory.shield:
      self.shield = True;
    elif item == Inventory.helmet:
      self.shield = True;
    elif item == Inventory.cloak:
      self.cloak = True;
    
  def buyWeapon(self, item):
    self.gold -= item.price;
    self.weapon = item;
    
  def buyArmor(self, item):
    self.gold -= item.price;
    self.armor = item;
    
  def useSpell(self):
    if self.knownSpell == "Mage Armor":
      self.spellText = ("Your armor becomes more effective!");
      self.baseArmor +=2;
    elif self.knownSpell == "Cloak of Shadows":
      self.spellText = ("You are much better at sneaking!");
      self.coreStealth +=3;
    elif self.knownSpell == "Fireball":
      self.spellText = ("You do substantial extra damage!");
      self.baseDamage += 3;
    elif self.knownSpell == "Levitation":
      self.spellText = ("You are much better at fleeing!")
      self.speedBonus += 4;
    self.knownSpell = "NONE";
    
  def wizLevel(self,hero,room):
    if hero.level == 1 and room.level > 4:
      hero.level = 2;
      self.knownSpell = Inventory.spells[random.randint(0,(len(Inventory.spells)-1))];
    elif hero.level == 2 and room.level >7:
      hero.level = 3;
      self.knownSpell = Inventory.spells[random.randint(0,(len(Inventory.spells)-1))];
  
  def profit(self, value):
    self.gold += value;