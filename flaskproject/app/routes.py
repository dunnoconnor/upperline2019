from app import app
from flask import render_template, request, redirect
from app.cliGame import inventory, explore, monster, encounter, loot, arsenal, town, character

inv = inventory.Inventory();
hero = character.Hero();
room = explore.Room(1);
enemy = monster.Monster(1);
event = encounter.Conflict();
store = town.Town();
item = loot.LootRoll(room.level);

def renderData(page):
    return render_template(page, name=hero.name, job=hero.job, level=hero.level, speed=hero.speed, strength=hero.strength, health=hero.health, gold=inv.gold, torches=inv.torches, rations=inv.rations, weapon=inv.weapon.name, weaponDamage= inv.weaponDamage, armor=inv.armor.name, helmet=inv.helmet, shield=inv.shield, cloak=inv.cloak, armorRating=inv.armorRating, stealthiness=inv.stealthiness, knownSpell=inv.knownSpell, descriptionA=room.descriptionA, descriptionB=room.descriptionB, descriptionC=room.descriptionC, lootTextA=item.lootTextA, lootTextB=item.lootTextB, introA=enemy.introA, introB=enemy.introB, introC=enemy.introC, introD=enemy.introD, resultA=event.resultA, resultB=event.resultB, resultC=event.resultC, counterA=event.counterA, counterB=event.counterB, counterC=event.counterC, storeWeapon=store.storeWeapon, storeArmor=store.storeArmor, storeGear=store.storeGear, spellText=inv.spellText);
    
@app.route('/')
@app.route('/index')
def gameStart():
    return renderData('game.html')

@app.route('/newGame', methods=['GET', 'POST'])
def adventureStart():
    hero.resetHero();
    return renderData('newGame.html');
    
@app.route('/confirmStart', methods=['GET', 'POST'])
def confirmStart():
    return renderData('chooseName.html');

@app.route('/sendName', methods=['GET', 'POST'])
def saveName():
    if request.method == "GET":
        return "error";
    else:
        data = dict(request.form);
        name = data['charName'];
        hero.setName(name);
        return renderData('chooseJob.html');

@app.route('/sendJob', methods=['GET', 'POST'])
def saveJob():
    if request.method == "GET":
        return "error";
    else:
        data = dict(request.form);
        job = data['jobButton'];
        job = job.upper();
        hero.setJob(job);
        hero.jobStats();
        inv.jobItems(job);
        if inv.torches>0:
            inv.burnTorch();
            room.resetDelve();
            return renderData('setOut.html');
        else:
            return renderData('setOutDark.html');

@app.route('/newRoom', methods=['GET', 'POST'])
def newRoom():
    if request.method == "GET":
        return "error";
    else:
        room.rollRoom(room.level);
        if room.monsterCount >= 1:
            enemy.rollMonster(room.level);
            event.resetConflict();
            return renderData(('monsterRoom.html'))
        else:
            item.rollLoot(room.level);
            inv.profit(item.value);
            return renderData('lootRoom.html');
            
@app.route('/monster', methods=['GET', 'POST'])
def monster():
    if request.method == "GET":
        return "error";
    else:
        data = dict(request.form);
        action = data['actionButton'];
        action = action.upper();
        event.chooseAction(hero, inv, enemy, action);
        if event.defeat == True:
            return renderData('defeat.html');
        elif event.victory == True:
            return renderData('victory.html');
        elif event.escape == True:
            return renderData('flee.html');
        else:
            return renderData('encounter.html');

@app.route('/resolve', methods=['GET', 'POST'])
def resolve():
    if request.method == "GET":
        return "error";
    else:
        data = dict(request.form);
        action = data['actionButton'];
        action = action.upper();
        event.chooseNextAction(hero, inv, enemy, action);
        if event.defeat == True:
            return renderData('defeat.html');
        elif event.victory == True:
            item.rollLoot(room.level);
            inv.profit(item.value);
            return renderData('victory.html');
        elif event.escape == True:
            return renderData('flee.html');
        else:
            return renderData('encounter.html');
            
@app.route('/crossroads', methods=['GET', 'POST'])
def crossroads():
    if request.method == "GET":
        return "error";
    else:
        if hero.job == "WIZARD":
            inv.wizLevel(hero, room);
        else:
            hero.levelUp(hero, room);
        room.delveDeeper();
        return renderData('crossroad.html');
    
                
@app.route('/crossroadSend', methods=['GET', 'POST'])
def directionChosen():
    if request.method == "GET":
        return "error";
    else:
        data = dict(request.form);
        direction = data['directionButton'];
        direction = direction.upper();
        if direction == "TOWN":
            store.rollTown();
            return renderData('town.html');
        elif direction == "REST":
            if inv.rations > 0:
                hero.heal();
            inv.eatRation();
            if (hero.job == "WIZARD") and (inv.knownSpell != "NONE"):
                inv.useSpell();
                return renderData('wizardCampsite.html');
            else:
                return renderData('campsite.html');
        else:
            room.rollRoom(room.level);
            if room.monsterCount >= 1:
                enemy.rollMonster(room.level);
                event.resetConflict();
                return renderData(('monsterRoom.html'))
            else:
                item.rollLoot(room.level);
                inv.profit(item.value);
                return renderData('lootRoom.html');                
            
            
@app.route('/sendShop', methods=['GET', 'POST'])
def shopping():
    if request.method == "GET":
        return "error";
    else:
        data = dict(request.form);
        purchase = data['buyButton'];
        purchase = purchase.upper();
        if purchase == "LEAVE":
            inv.checkItemEffects();
            if inv.torches>0:
                inv.burnTorch();
                room.resetDelve();
                return renderData('setOut.html');
            else:
                return renderData('setOutDark.html');
        elif purchase == "TORCH":
            if store.torch.price <= inv.gold:
                inv.buyTorch();
            return renderData(('town.html'));
        elif purchase == "RATION":
            if store.ration.price <= inv.gold:
                inv.buyRation();
            return renderData(('town.html'));
        elif purchase == "WEAPON":
            if store.weapon.price <= inv.gold:
                inv.buyWeapon(store.weapon);
            return renderData(('town.html'));
        elif purchase == "ARMOR":
            if store.armor.price <= inv.gold:
                inv.buyArmor(store.armor);
            return renderData(('town.html'));
        elif purchase == "GEAR":
            if store.gear.price <= inv.gold:
                inv.buyGear(store.gear);
            return renderData(('town.html'));
        elif purchase == "TAVERN":
            if store.tavern.price <= inv.gold:
                return renderData(('endGame.html'));
            else:
                return renderData(('town.html'));
                
     
            
            
