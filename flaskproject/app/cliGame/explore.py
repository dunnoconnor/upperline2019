import random
from random import randint


class Room:
  
  adjectives = [" dark"," small"," great"," deep"," natural"," big"," sacred"," secret"," shallow"," huge"," rocky"," vast"," main"," hidden"," black"," gloomy"," dry"," inner"," hollow"," narrow"," artificial"," ancient"," lonely"," large"," damp"," cold"," cool"," mysterious"," tiny"," remarkable"," warm"," crystal"," spacious"," smaller"," remote"," beautiful"," enormous"," prehistoric"," mammoth"," dim"," solitary"," wonderful"," magic"," enchanted"," vacant"," double"," corycian"," sepulchral"," cut"," immense"," shadowy"," coral-like"," strange"," deep"," darksome"," curious"];
  areas = ["chamber","clearing","area","glade","wood","swamp","forest","cave","ruin","dungeon","wetland","mire","cavern","patch of darkness","space","cavern","grotto","cavity","den","hollow","pothole","rock shelter","subterranean area","tunnel","dugout","hole"]
  density = ["with","full of","marked by","and spot","and see","and note"]
  sights = ["tangles of dark ivy","ancient oaks","pines","white birch trees","yellow lichen","thick mosses","strange mushrooms","creeping vines","withered ferns","dead trees","burned trees","piles of ash","rotting wood","small puddles","rivulets of water","strange, chalky stones","glowing fungus","shattered weapons","skeletons","gravestones","pools of water","crumbling ruins","neglected stone walls","broken furniture","rusted tools","dried bones","stalactites","stalagmites","piles of guano","bits of rusted metal","corpses","spider eggs","spider webs","tombs","stone cairns","strange carvings","cave paintings","unknown glyphs","claw-marks in the dirt","wide roots","thorn bushes","poisonous berries","peat bogs","thin reeds","round stones","animal tracks","tufts of fur"];
  smells = [ " abominable"," acid"," acrid"," agreeable"," ammoniacal"," animal"," antiseptic"," appetizing"," aromatic"," awful"," bad"," beautiful"," better"," bitter"," briny"," burnt"," chemical"," clean"," cloying"," coppery"," curious"," damp"," dank"," delicious"," delightful","","different"," disagreeable"," disgusting"," distinct"," distinctive"," dreadful"," dry"," dusty"," earthy"," enticing"," evil"," familiar"," fetid"," fine"," fishy"," flowery"," foetid"," foul"," fragrant"," fresh"," fruity"," funky"," funny"," glorious"," good"," greasy"," great","green"," harsh"," heady"," heavenly"," heavy"," homely"," horrible"," horrid"," hot"," ill"," indescribable"," intense"," intolerable"," keen"," like"," lingering"," little"," lovely"," medicinal"," metallic"," moist"," moldy"," mouldy"," musky"," musty"," nasty"," natural"," nauseating"," nauseous"," new"," nice"," noisome"," noxious"," odd"," offensive"," oily"," old"," only"," other"," overpowering"," overwhelming"," own"," particular"," peculiar"," penetrating"," pervading"," pervasive"," pleasant"," pleasing"," potent"," powerful"," pungent"," putrid"," rancid"," rank"," raw"," refreshing"," repulsive",""," resinous"," rich"," ripe"," rotten"," rotting"," salty"," savory"," savoury"," sharp"," sick"," sickening"," sickly"," skunk"," slight"," smoke"," smoky"," soapy"," soft"," sour"," special"," spicy"," stale"," stifling"," stinking"," strange"," strong"," stronger"," stuffy"," subtle"," suffocating"," sulfurous"," sulphureous","","sulphurous"," sure"," sweaty"," sweet"," sweeter"," sweetest"," sweetish"," tangy"," tantalizing"," terrible"," thick"," unfamiliar"," unique"," unmistakable"," unpleasant"," unusual"," unwholesome"," vague"," vile"," weird"," wholesome"," wonderful"," woodsy"," woody"];
  tones = ["boisterous","low-pitched","shrill","brittle","mellifluous","silent","calm","melodic","smooth","clamorous","melodious","soft","croaky","muffled","soundless","discordant","musical","dissonant","muted","squeaky","dull","noiseless","strong","earsplitting","noisy","sweet","enjoyable","faint","gentle","piercing","thundering","gruff","pleasing","thunderous","half-deafening","quiet","tranquil","rasping","tuneful","harmonious","raspy","harsh","raucous","high","resonant","velvety","high-pitched","riotous","hoarse","husky","screaky","whispered","loud","screaming","low"];
  sounds = ["screech","bark","peep","twittering","trill","cheep","chirp","hoot","squeak","song","call","click","wheeze","clack","clatter","grating","grinding","growl","swish","shriek","squawk","cluck","cackle","ping"];
  feels = ["muggy","sweltering","pressing","thick","languid","sticky","suffocating","gray","misty","soupy","perfumed","swift","lively","breezy","aromatic","chemically","charged","prickly","lifeless","spicy","light","malodorous","clear","hazy","dirty","uplifting","fresh","smoky","dreary","flat","oily","tepid","lukewarm","toxic","boiling"];

  def __init__(self, level):
    self.level = level;
    self.adjective = Room.adjectives[random.randint(0,len(Room.adjectives)-1)];
    self.area = Room.areas[random.randint(0,len(Room.areas)-1)];
    self.density = Room.density[random.randint(0,len(Room.density)-1)];
    self.sight = Room.sights[random.randint(0,len(Room.sights)-1)];
    self.smell = Room.smells[random.randint(0,len(Room.smells)-1)];
    self.tone = Room.tones[random.randint(0,len(Room.tones)-1)];
    self.sound = Room.sounds[random.randint(0,len(Room.sounds)-1)];
    self.feel = Room.feels[random.randint(0,len(Room.feels)-1)];
    self.monsterCount = random.randint(0,4);
    self.lootCount = random.randint(0,2);
    self.descriptionA = ("You enter a" + self.adjective + " " + self.area + " " + self.density + " " + self.sight + ".");
    self.descriptionB = ("You hear a " + self.tone + " " + self.sound + ".\n");
    self.descriptionC = ("The air is " + self.feel + " and smells" + self.smell + ".\n" );

  def rollRoom(self, level):
    self.level = level;
    self.adjective = Room.adjectives[random.randint(0,len(Room.adjectives)-1)];
    self.area = Room.areas[random.randint(0,len(Room.areas)-1)];
    self.density = Room.density[random.randint(0,len(Room.density)-1)];
    self.sight = Room.sights[random.randint(0,len(Room.sights)-1)];
    self.smell = Room.smells[random.randint(0,len(Room.smells)-1)];
    self.tone = Room.tones[random.randint(0,len(Room.tones)-1)];
    self.sound = Room.sounds[random.randint(0,len(Room.sounds)-1)];
    self.feel = Room.feels[random.randint(0,len(Room.feels)-1)];
    self.monsterCount = random.randint(0,4);
    self.lootCount = random.randint(0,2);
    self.descriptionA = ("You enter a" + self.adjective + " " + self.area + " " + self.density + " " + self.sight + ".");
    self.descriptionB = ("You hear a " + self.tone + " " + self.sound + ".\n");
    self.descriptionC = ("The air is " + self.feel + " and smells" + self.smell + ".\n" );
    
  def delveDeeper(self):
    self.level += 1;
    
  def resetDelve(self):
    self.level = 1;
      
  