$('.dropdown-trigger').dropdown();

//arrays of character data
var jobs = ["Witch","Warg-keeper ","Hornblower","Scavenger","Thief","Woodcutter","Scout","Trader","Charlatan","Sapper","Pit Fighter","Cook","Sailor","Tinker","Forge Smithy","Hunter","Ditch Digger","Sawbones","Spear Carrier","Miner"];
var age = ["Green-ear", "Longtooth", "Roughneck", "Greybeard"];
var garb = ["Goat Skull","Tooth Necklace","Tunic","Eyepatch","Hood","Warm Hat",'"Fancy" Shoes',"Scarf",'"Fancy" Hat',"Heavy Boots","Leather Pauldron","Bloody Apron","Striped Pants","Goggles","Iron Mask","Ragged Pelt","Loin Cloth","Heavy Gloves","Warpaint","Cloak"];
var boss = ["Died", "Went Broke", "Got Kidnapped", "Fired You", "Ran Off", "Tossed in the Brig"];
var xp = ["Personal Insight", "Humbling Failure", "Trial by Fire", "Modest Accomplishment", "Motivating Loss", "Indebtedness to Another Goblin"];
var traitCount = 0;
var weapons = ["Club", "Staff", "Rusty Knife", "Broken Bottle", "Sharpened Stick", "Sling and Stones"];
var gear = ["(Some Herbs)","(Whistle)","(Horn)","(Some Twine)","(Bag of Sand)","(Hatchet)","(Spyglass)","(Pack)","(Fake Coins)","(Wire Cutters)","(Iron Knuckles)","(Pot)","(Dice)","(Wrench)","(Nails)","(Javelin)","(Shovel)","(Bonesaw)","(Spear)","(Pick)"];
var items = ["20 Feet of Rope", "Vial of Poison", "Random Spell", "Small Hammer", "Rat", "Burlap sack"];
var spells = ["Dead Tongue", "Liar's Whistle", "Heavy Eye", "Fiery Gaze", "Breath of Fog", "Enlightened Quill"];

//populate jobs
for(var i=0; i< jobs.length;i++){
    $("#dropdownJob").append('<li><a href="#!">'+jobs[i]+'</a></li>');
}

//choose job
$('#dropdownJob li').click(function(){
    a = $(this).text();
    $('.displayJob').text(a);
    var gearIndex = jobs.indexOf(a);
    document.querySelector(".displayGear").innerHTML = (gear[gearIndex]);
})

//roll job
function rollJob() {
    var jobIndex = Math.floor((Math.random() * jobs.length));
    document.querySelector(".displayJob").innerHTML = (jobs[jobIndex]);
    document.querySelector(".displayGear").innerHTML = (gear[jobIndex]);
};

//populate ages
for(var i=0; i< age.length;i++)
{
$("#dropdownAge").append('<li><a href="#!">'+age[i]+'</a></li>');
}

//choose age
$('#dropdownAge li').click(function(){
    a = $(this).text()
    $('.displayAge').text(a)
})

//roll age
function rollAge() {
    var ageIndex = Math.floor((Math.random() * age.length));
    document.querySelector(".displayAge").innerHTML = (age[ageIndex]);
};

//populate garb
for(var i=0; i< garb.length;i++)
{
$("#dropdownGarb").append('<li><a href="#!">'+garb[i]+'</a></li>');
}

//choose garb
$('#dropdownGarb li').click(function(){
    a = $(this).text()
    $('.displayGarb').text(a)
})

//roll garb
function rollGarb() {
    var garbIndex = Math.floor((Math.random() * garb.length));
    document.querySelector(".displayGarb").innerHTML = (garb[garbIndex]);
};

//populate bosses
for(var i=0; i< boss.length;i++)
{
$("#dropdownBoss").append('<li><a href="#!">'+boss[i]+'</a></li>');
}

//choose boss
$('#dropdownBoss li').click(function(){
    a = $(this).text()
    $('.displayBoss').text(a)
})

//roll boss
function rollBoss() {
    var bossIndex = Math.floor((Math.random() * boss.length));
    document.querySelector(".displayBoss").innerHTML = (boss[bossIndex]);
};

//populate xps
for(var i=0; i< xp.length;i++)
{
$("#dropdownXP").append('<li><a href="#!">'+xp[i]+'</a></li>');
}

//choose xp
$('#dropdownXP li').click(function(){
    a = $(this).text()
    $('.displayXP').text(a)
})

//roll xp
function rollXP() {
    var xpIndex = Math.floor((Math.random() * xp.length));
    document.querySelector(".displayXP").innerHTML = (xp[xpIndex]);
};


//add trait
function addTrait() {
    if (traitCount<3){
        traitCount++;
    } else {
        traitCount = 1;
    }
    document.querySelector(".trait"+traitCount).innerHTML = document.getElementById("traitInput").value;
    document.getElementById("traitInput").value = "";
};

//add name
function addName() {
    document.querySelector(".displayName").innerHTML = document.getElementById("nameInput").value;
    document.getElementById("nameInput").value = "";
};

//add title
function addTitle() {
    document.querySelector(".displayTitle").innerHTML = document.getElementById("titleInput").value;
    document.getElementById("titleInput").value = "";
};

//add outlook
function addOutlook() {
    document.querySelector(".displayOutlook").innerHTML = document.getElementById("outlookInput").value;
    document.getElementById("outlookInput").value = "";
};

//add goal
function addGoal() {
    document.querySelector(".displayGoal").innerHTML = document.getElementById("goalInput").value;
    document.getElementById("goalInput").value = "";
};

//populate weapons
for(var i=0; i< weapons.length;i++)
{
$("#dropdownWeapon").append('<li><a href="#!">'+weapons[i]+'</a></li>');
}

//choose weapon
$('#dropdownWeapon li').click(function(){
    a = $(this).text()
    $('.displayWeapon').text(a)
})

//roll weapon
function rollWeapon() {
    var weaponIndex = Math.floor((Math.random() * weapons.length));
    document.querySelector(".displayWeapon").innerHTML = (weapons[weaponIndex]);
};

//populate item
for(var i=0; i< items.length;i++)
{
$("#dropdownItem").append('<li><a href="#!">'+items[i]+'</a></li>');
}

//choose item
$('#dropdownItem li').click(function(){
    a = $(this).text();
    $('.displayItem').text(a);
    if (items.indexOf(a)== 2){
        var spellIndex = Math.floor((Math.random() * spells.length));
        document.querySelector(".displaySpell").innerHTML = (spells[spellIndex]);
    } else {
        document.querySelector(".displaySpell").innerHTML = ("");
    }
})

//roll item
function rollItem() {
    var itemIndex = Math.floor((Math.random() * items.length));
    document.querySelector(".displayItem").innerHTML = (items[itemIndex]);
    if (itemIndex == 2){
        var spellIndex = Math.floor((Math.random() * spells.length));
        document.querySelector(".displaySpell").innerHTML = (spells[spellIndex]);
    } else {
        document.querySelector(".displaySpell").innerHTML = ("");
    }
};