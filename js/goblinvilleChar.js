console.log("connected");

var age = ["green-ear", "long-tooth", "roughneck", "greybeard"];
var jobs = ["Witch","Warg-keeper ","Hornblower","Scavenger","Thief","Woodcutter","Scout","Trader","Charlatan","Sapper","Pit fighter","Cook","Sailor","Tinker","Forge Smithy","Hunter","Ditch digger","Sawbones","Spear carrier","Miner"];
var gear = ["some herbs","a whistle","a horn","some twine","a bag of sand","a hatchet","a spyglass","a pack","some fake coins","wire cutters","iron knuckles","a pot","some dice","a wrench","some nails","a javelin","a shovel","a bonesaw","a spear","a pick"];
var garb = ["a goat skull","a tooth necklace","a tunic","an eyepatch","a hood","a warm hat",'"fancy" shoes',"a scarf",'a "fancy" hat',"heavy boots","a single leather pauldron","a bloody apron","striped pants","goggles","an iron mask","a ragged pelt","a loin cloth","heavy gloves","warpaint","a cloak"];
var xp = ["a personal insight", "a humbling failure", "a trial by fire", "a modest accomplishment", "a motivating loss", "an indebtedness to another goblin (ask who)"];
var bossFate = ["died", "went broke", "got kidnapped", "fired you", "ran off", "got tossed in the brig"];
var weapons = ["club", "staff", "rusty knife", "broken bottle", "sharpened stick", "sling and stones"];
var items = ["20 feet of rope", "a vial of poison", "a random spell", "a small hammer", "a rat", "a burlap sack"];
var name = ""

function setName() {
    
}

function updateText() {
            var ageIndex = Math.floor((Math.random() * age.length));
            var jobIndex = Math.floor((Math.random() * jobs.length));
            var garbIndex = Math.floor((Math.random() * garb.length));
            var xpIndex = Math.floor((Math.random() * xp.length));
            var bossIndex = Math.floor((Math.random() * bossFate.length));
            var itemIndex = Math.floor((Math.random() * items.length));
            var weaponIndex = Math.floor((Math.random() * weapons.length));

            var thisAge = age[ageIndex];
            var thisJob = jobs[jobIndex];
            var thisGear = gear[jobIndex];
            var thisGarb = garb[garbIndex];
            var thisExperience = xp[xpIndex];
            var thisBossFate = bossFate[bossIndex];
            var thisItem = items[itemIndex];
            var thisWeapon = weapons[weaponIndex];

            document.querySelector(".first").innerHTML = ("You are " + name + ", a" + thisAge + " " + thisJob + "  wearing " + thisGarb +". You experienced " + thisExperience + " and then your boss " + thisBossFate + ".");
            document.querySelector(".second").innerHTML =  ("You are carrying 2 rations, 2 torches, " + thisGear + ", and " + thisItem + ". You are wielding a " + thisWeapon + "." );
};
