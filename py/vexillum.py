import sys;

pack = True;
exhausted = False;

def intro():
    print("The Vexillum");
    print(" ")
    print("A Story of Fallen Empires");
    print("by Michael Dunn-O'Connor");
    print(" ")
    input("Press Enter to Begin  ");
    print(" ");
    print("You stumble through the thick spring mud, your path lit by a white pinprick of sunlight wheeling across the red-brown scab of twilight.");
    input("...");
    print(" ");
    print("Your pack weighs heavy on your back and every step draws your boots into the reeking black earth.");
    input("...");    
    print(" ");
    print("You hear the slurping sound behind you, the low call of the worm eaters.  They will catch you sooner or later.");
    print("Your pack laden with precious saltblocks, and the weight is slowing you down considerably.")
    input("...");
    print(" ");
    checkStart();

def checkStart():
    global pack;
    startPrompt = input("Do you PUSH ON or DROP THE PACK?  ");
    print(" ");
    if startPrompt.upper() == 'PUSH ON':
        exhausted = True;
        pushOn();
    elif startPrompt.upper() == 'DROP THE PACK':
        pack = False;
        pushOn();
    else:
        checkStart();

def pushOn():
    print(" ");
    global pack;
    if (pack == True):
        exhausted = True;
        print("You trudge on, remembering that the Vexillum will need the stolen salt you carry.");
    else:
        print("You move faster without the pack, though the Vexillum will miss the salt it carried.");
    input("...");
    print(" ");
    print("Even in summer, the army can't survive on fresh hunt and forage alone.");
    print("Salt helps the army preserve as much as possible while you make your way North.");
    input("...");
    print(" ");
    print("You keep walking, for endless red hours until the sky begins to turn pinkish gold.");
    print("Back when the sun still rose and set, they called this dawn.");
    input("...");
    print(" ");
    print("The worm eaters have kept their distance, likely waiting for you to rest.");
    print("You could press on, but there must be other members of your centurae that survived the Frankish attack.");
    print("It would better to travel in force.");
    input("...");
    print(" ");
    checkSearch();

def checkSearch():
    searchPrompt = input("Do you TRAVEL ALONE or SEARCH for the other soldiers?  ");
    print(" ");
    if searchPrompt.upper() == 'TRAVEL ALONE':
        alone();
    elif searchPrompt.upper() == 'SEARCH':
        search();
    else:
        checkSearch();
    
def alone():
    print(" ");
    print("You move quickly through the swamps, your uniform drenched and your legs weary.")
    print("You see the pine forests on the Nothern horizon.  The Vexilllum is camped somewhere within.")
    input("...");
    print(" ")
    print("As you reach the line of dense gray trees, needles brown for lack of light, you see torches dancing in the shadows.");
    print("If these are Franks, they'll kill you on sight.")
    input("...");
    print(" ")
    checkAlone();
    
def checkAlone():
    alonePrompt = input("Do you CALL OUT to them or RUN for it?  ");
    print(" ");
    if alonePrompt.upper() == 'CALL OUT':
        surrender();
    elif alonePrompt.upper() == 'RUN':
        run();
    else:
        checkAlone();
        
def surrender():
    print(" ");
    print("You throw your hands to the red sky, and step forward from your hiding place.")
    print("You pray that you will live to see your Vexillum again, those who still march beneath the banner of Rome.")
    print("The riders send a patrol out in to the surrounding marsh, to be sure you are not baiting a trap.")
    input("...");
    print(" ");
    print("If only it were so.  Eventually, a small party approaches.");
    print("You look up, through a haze, at the leader above you.  Not Frankish, it seems.")
    print("He is a huge man, with a curly red beard.  The hair on his head is braided, and glistening with lard.");
    input("...");
    print(" ");
    print("He reeks of garlic and elk.  A Burgundian.");
    print("He asks what you would trade for your life.");
    input("...");
    print(" ");
    checkSurrender();

def checkSurrender():
    global pack;
    if pack == False:
        print("Without your pack full of salt, you have nothing to offer.");
        print("They bind your shackles tight.");
        input("...");
        print(" ");
        print("They pull you along on a lead, presumably toward the Burgundian camp.");
        print("You wonder if you will ever see the banners of the Vexillum again.")
        input("...");
        print(" ");
        end();
    else:
        pack = False;
        print("You tear open you pack, showing the blocks of salt within.");
        print("The Burgundians accept your offer and climb back into their saddles.");
        input("...");
        print(" ");
        print("They fade into the forest like shadows, leaving you alone in the muddy field.");
        print("You press on alone, giving their company a wide berth.");
        input("...");
        print(' ');
        plains();
        
def run():
    global pack;
    if (pack == True):
        print("You turn and flee but your heavy pack weighs you down.");
        print("They cut you down within minutes.");
        print("The blood seeps from wide wounds on your back, into the mud below.");
        input("...");
        print(" ");
        print("You look up, through a haze, at the leader above you.");
        print("Not Frankish, it seems.  He is a huge man, with a curly red beard.");
        input("...");
        print(" ");
        print("The hair on his head is braided, and glistening with lard.");
        print("He reeks of garlic and elk.  A Burgundian.");
        input("...");
        print(" ");
        die();

    else:
        print("You sprint clear across the muddy plains.");
        print("They persue you briefly, but do not follow into the lands of the worm eaters.");
        print("When you come to rest, your bones are weary and your breath ragged.");
        input("...");
        print(" ");
        plains();

def search():
    global pack;
    global exhausted;
    if pack == True:
        exhausted = True;
        print("Your pack weighs heavy on your shoulders.")
    print("You search the muddy plains for signs of another lost solider.");
    print("After hours of fruitless searching, you notice something on the horizon.");
    input("...");
    print(" ");
    print("The hill south of you is dotted with hunched, hairless figures.");
    print("You see the sunlight glinting off rows of ragged teeth.");
    input("...");
    print(" ");
    print("The worm eaters don't eat men, but they take them.  Some say they bury their captives alive.");
    print("Somewhere across the black expanse that was once Northern Italia, the Vexillum is waiting");
    print("You have no choice but to press on.");
    input("...");
    print(" ");
    print("Traveling North through the forests is the more direct route, but you could also march West to the sea.")
    input("...");
    print(" ");
    checkRoute();
    
def checkRoute():
    routePrompt = input("Do you travel NORTH or WEST?  ");
    print(" ");
    if routePrompt.upper() == 'NORTH':
        plains();
    elif routePrompt.upper() == 'WEST':
        sea();
    else:
        checkRoute();
    
def sea():
    print(" ");
    print("You walk for the sea, but hours of walking seem to bring it no closer.");
    print("You see the steaming green waters from afar, and the bleached bones of great fish scatter the shore.");
    input("...");
    print(" ");
    print("But you will need to rest before you get there.");
    input("...");
    print(" ");
    print("You find an outcropping of gray stone and take cover beneath it.");
    print("You set yourself down on the moist earth and close your eyes.");
    input("...");
    print(" ");
    print("Sleep comes quickly.");
    input("...");
    sleep();
    
def plains():
    global exhausted;
    if exhausted == True:
        print("Near the forest edge, you trip on a stone and collapse into the stinking mud at your feet.");
        print("You are too weak to pull yourself up.");
        input("...");
        print(" ");
        print("Sleep comes quickly.");
        input("...");
        sleep();
    else:
        print("You make it clear to the forest and step into the shade beneath the withered grey pines.");
        print("You stumble along through most of the night before a guard finds you.")
        input("...");
        print("");
        print("She leads you back to the camp, and you can smell the cookfire and hear the far off laughter.");
        print("You made it to the Vexillum encampment.  You are home.")
        input("...");
        print(" ");
        end();

def sleep():
    print(" ")
    print("When you wake you are in a cold, dusty city.");
    print("White stone walls tower over you on all sides.");
    input("...");
    print(" ");
    print("Then you hear it, like a rusted iron hinge turning over and over, shaking your skull and bringing tears to your eyes.");
    print("You must still be asleep, and the Maelstrom has found you.");
    input("...");
    print(" ");
    print("You need to regain your senses before it consumes you.");
    input("...");
    print(" ");
    checkSleep();

def checkSleep():
    sleepPrompt = input("Do you SCREAM or SLAP yourself?  ");
    print(" ");
    if sleepPrompt.upper() == 'SCREAM':
        print("You scream and scream until you are weak.");
        print("But eventually you wear yourself out.");
        input("...");
        print(" ");        
        print("It feels as if you were always on your way here, without ever having known it.");
        print("A gaunt man, covered heaad to toe in dust, comes to place a comforting hand upon your shoulder.");
        print("You look up at his face and sees his mouth is sewn shut with thick black wire.");
        input("...");
        print(" ");
        print("You awaken.");
        input("...");
        print(' ');
        awaken();
    elif sleepPrompt.upper() == 'SLAP':
        print("You slap yourself and tear at your hair until you are weak.");
        print("But eventually you wear yourself out.");
        input("...");
        print(" ");
        print("It feels as if you were always on your way here, without ever having known it.");
        print("A gaunt man, covered heaad to toe in dust, comes to place a comforting hand upon your shoulder.");
        print("You look up at his face and sees his mouth is sewn shut with thick black wire.");
        input("...");
        print(" ");
        print("You awaken.");
        input("...");        
        print(' ');
        awaken();
    else:
        checkSleep();
        
def awaken():
    print("You force open your eyes and struggle to reorient yourself.");
    print("But it is too late.");
    input("...");
    print(" ");
    print("You are in a shallow grave, pinned down by heavy stones upon your chest.");
    print("The worm eaters have found you in your sleep.");
    input("...");
    print(" ");
    print("They are burying you here.");
    print("Everything goes dark as they finish pouring handfuls of dirt over your face, slurping quietly.");
    input("...");
    print(" ");
    die();
    
def die():
    input("...");
    print(" ");
    print("Your last thoughts are of your of the Vexillum, those who still march beneath the banner of Rome.");
    print("You should have died among them.");
    input("...");
    print(" ");
    print("You died a legionary, Marcus Signus.  The Vexillum lives on.");
    input("...");
    print(" ");
    end();

def end():
    print("fin");
    input("...");
    print(" ");
    print(" ");
    checkReset();
    
def checkReset():
    print("Do you want to play again?");
    print(" ");
    resetPrompt = input("Type YES or NO.  ");
    print(" ");
    if resetPrompt.upper() == 'YES':
        intro();
    elif resetPrompt.upper() == 'NO':
        print(" ");
    else:
        checkReset();

intro();
