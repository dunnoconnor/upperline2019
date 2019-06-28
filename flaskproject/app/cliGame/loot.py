import random
from random import randint


class LootRoll:
  
  badQualities = ["busted","collapsed","cracked","crumbling","crushed","damaged","defective","fractured","fragmented","mangled","severed","shattered","smashed","disintegrated","dismembered","pulverized","rent","riven","shredded","slivered","split","frayed","shabby","tattered","timeworn","well-worn","beat","destroyed","deteriorated","dinged","overused","overworked","ragged","ruined","totaled","haggard","decaying","blighted","corrupted","decomposing","dilapidated","moldy","rotting","rusted"];
  standardQualities = ["basic","classic","common","normal","typical","average","boilerplate","stock","everyday","garden variety","run-of-the-mill","mediocre","ordinary","regular","commonplace","fair","humdrum","intermediate","middling","standard","customary","fair to middling","garden-variety","middle of the road","passable","run of the mill","so-so","tolerable","unexceptional"];
  goodQualities = ["attractive","beautiful","cool","elegant","exceptional","exquisite","fashionable","first-rate","great","handsome","lovely","magnificent","neat","outstanding","rare","solid-looking","splendid","striking","subtle","superior","well-made","choice","mean","first-class","five-star","gilt-edged","gnarly","good-looking","ornate","showy","supreme","top-notch","unreal","wicked","durable","dependable","flawless","reliable","solid","sturdy","invaluable","heirloom","inestimable","precious","serviceable","complicated","lavish","special","sumptuous","adorned","baroque","beautifying","custom","decorated","elaborate","embellished","garnished","rococo","intricate","ostentatious","resplendent","spiffy","unusual"];
  sources = ["ancient","antique","human","elven","dwarven","goblin","orcish","iron","dragon bone","silver","copper","bronze","steel","occult","mystical","brass","obsidian"];
  lootTypes = ["basin","bottle","can","flask","jug","pot","urn","vase","vessel","beaker","burette","chalice","crock","cruet","decanter","ewer","flagon","pitcher","tun","vat","bracelet","brooch","earring","jewel","knickknack","necklace","ornament","pendant","tiara","treasure","trinket","adornment","anklet","band","bangle","bauble","bead","cameo","chain","charm","crown","locket","pin","ring","coin","ingot"];

  def __init__(self, level):
    randomQuality = level + random.randint(0,2);
    if randomQuality > 5:
      self.quality = LootRoll.goodQualities[random.randint(0,len(LootRoll.goodQualities)-1)];
    elif randomQuality > 2:
      self.quality = LootRoll.standardQualities[random.randint(0,len(LootRoll.standardQualities)-1)];
    else:
      self.quality = LootRoll.badQualities[random.randint(0,len(LootRoll.badQualities)-1)];
    self.value = randomQuality;
    self.quality = LootRoll.badQualities[random.randint(0,len(LootRoll.badQualities)-1)];
    self.source = LootRoll.sources[random.randint(0,len(LootRoll.sources)-1)];
    self.lootType = LootRoll.lootTypes[random.randint(0,len(LootRoll.lootTypes)-1)];
    self.lootTextA = ("You find a " + self.quality + " " + self.source + " " + self.lootType + ".");
    self.lootTextB = ("It's worth " + str(self.value) + " gold.");

  def rollLoot(self,level):
    randomQuality = level + random.randint(0,2);
    if randomQuality > 5:
      self.quality = LootRoll.goodQualities[random.randint(0,len(LootRoll.goodQualities)-1)];
    elif randomQuality > 2:
      self.quality = LootRoll.standardQualities[random.randint(0,len(LootRoll.standardQualities)-1)];
    else:
      self.quality = LootRoll.badQualities[random.randint(0,len(LootRoll.badQualities)-1)];
    self.value = randomQuality;
    self.quality = LootRoll.badQualities[random.randint(0,len(LootRoll.badQualities)-1)];
    self.source = LootRoll.sources[random.randint(0,len(LootRoll.sources)-1)];
    self.lootType = LootRoll.lootTypes[random.randint(0,len(LootRoll.lootTypes)-1)];
    self.lootTextA = ("You find a " + self.quality + " " + self.source + " " + self.lootType + ".");
    self.lootTextB = ("It's worth " + str(self.value) + " gold.");
