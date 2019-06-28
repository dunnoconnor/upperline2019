import random
from random import randint

class Monster:
  
  titles =["beast","beast","demon","devil","horror","brute","colossus","fiend","hellion","monstrosity","mutant","creature","creature","monster","monster","fiend","quadruped","biped","thing borne of nightmares"];
  parts = ["a crocodile","a vulture"," a wild Dog","a Snapping Turtle","an Alligator","a Black Bear","an Anaconda","a Condor","a Bald Eagle","a Tiger","a Piranha","a Rat","a Jackal","a Shark","a Hyena","Lynx","a Baboon","a Cheetah","a Chimpanzee","a Leopard","an Octopus","a Cougar","a Coyote","a Dingo","a Rattlesnake","a Badger","a Giant Squid","a Gila Monster","a Golden Eagle","a Gray Wolf","a Barracuda","a Hammerhead Shark","a Great White Shark","a Moray Eel","a Jaguar","a Komodo Dragon","a Kraken","a Leviathan","a Lion","a Mandrill","an Ocelot","a Peregrine Falcon","a Polar Bear","a Sea Serpent","a Snow Leopard","a Tasmanian Devil","a Walrus","a Wolverine"];
  descriptors = ["horrifying","intimidating","horrendous","spine-chilling","unnerving","acute","pointed","razor-sharp","sharpened","stinging","fine","keen","tapering","acuate","acuminate","acuminous","apical","barbed","briery","cuspate","cuspidate","edged","ground fine","honed","horned","jagged","keen-edged","knife-edged","needle-pointed","needlelike","peaked","pointy","prickly","pronged","serrated","sharp-edged","spiked","spiky","spiny","splintery","tapered","thorny","tined","deadly","fatal","nasty","perilous","terrible","threatening","treacherous","formidable","malignant","menacing","portentous","wicked"];
  weapons = ["teeth","claws","barbed tail","jaws","paws","talons","beak","pincers","quills","spores","fangs","fists","hooves","horns","tusks","tentacles","hooks","spurs","antlers","mandibles"];
  modifiers = ["about","roughly","approximately","practically","easily"];
  sizes = ["a dog","a man", "an ox", "an elephant", "a building"];

  def __init__(self, level):
    self.title = Monster.titles[random.randint(0,len(Monster.titles)-1)];
    headNum = random.randint(0,len(Monster.parts)-1);
    bodyNum = random.randint(0,len(Monster.parts)-1);
    while bodyNum == headNum:
      bodyNum = random.randint(0,len(Monster.parts)-1);
    self.head = (Monster.parts[headNum]).lower();
    self.body = (Monster.parts[bodyNum]).lower();
    self.descriptor = Monster.descriptors[random.randint(0,len(Monster.descriptors)-1)];
    self.weapon = Monster.weapons[random.randint(0,len(Monster.weapons)-1)];
    self.range = random.randint(0,3);
    if self.range > 1:
      self.rangeTerm = "from afar";
    else:
      self.rangeTerm = "up close";
    self.modifier = Monster.modifiers[random.randint(0,len(Monster.modifiers)-1)];
    sizeRoll = random.randint(0,level);
    if sizeRoll > (len(Monster.sizes)-1):
      self.size = Monster.sizes[(len(Monster.sizes)-1)];
    else:
      self.size = Monster.sizes[sizeRoll];
    self.damage = (random.randint(0,level) + sizeRoll + 1);
    self.health = (random.randint(0,level) + sizeRoll + 4);
    self.armor = sizeRoll;
    self.introA = ("You see a " + self.title + " with the head of " + self.head + " and the body of " + self.body + ".");
    self.introB = ("It is " + self.modifier + " the size of " + self.size + ".");
    self.introC = ("Its " + self.descriptor + " " + self.weapon + " can inflict " + str(self.damage) + " DAMAGE " + self.rangeTerm + ".");
    self.introD = ("It has " + str(self.health) + " HEALTH and " + str(self.armor) + " ARMOR.\n");

  def rollMonster(self, level):
    self.title = Monster.titles[random.randint(0,len(Monster.titles)-1)];
    headNum = random.randint(0,len(Monster.parts)-1);
    bodyNum = random.randint(0,len(Monster.parts)-1);
    while bodyNum == headNum:
      bodyNum = random.randint(0,len(Monster.parts)-1);
    self.head = (Monster.parts[headNum]).lower();
    self.body = (Monster.parts[bodyNum]).lower();
    self.descriptor = Monster.descriptors[random.randint(0,len(Monster.descriptors)-1)];
    self.weapon = Monster.weapons[random.randint(0,len(Monster.weapons)-1)];
    self.range = random.randint(0,3);
    if self.range > 1:
      self.rangeTerm = "from afar";
    else:
      self.rangeTerm = "up close";
    self.modifier = Monster.modifiers[random.randint(0,len(Monster.modifiers)-1)];
    sizeRoll = random.randint(0,level);
    if sizeRoll > (len(Monster.sizes)-1):
      self.size = Monster.sizes[(len(Monster.sizes)-1)];
    else:
      self.size = Monster.sizes[sizeRoll];
    self.damage = (random.randint(0,level) + sizeRoll + 1);
    self.health = (random.randint(0,level) + sizeRoll + 4);
    self.armor = sizeRoll;
    self.introA = ("You see a " + self.title + " with the head of " + self.head + " and the body of " + self.body + ".");
    self.introB = ("It is " + self.modifier + " the size of " + self.size + ".");
    self.introC = ("Its " + self.descriptor + " " + self.weapon + " can inflict " + str(self.damage) + " DAMAGE " + self.rangeTerm + ".");
    self.intoD = ("It has " + str(self.health) + " HEALTH and " + str(self.armor) + " ARMOR.\n");
    