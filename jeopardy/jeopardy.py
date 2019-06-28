
from difflib import SequenceMatcher
import requests
import random
from random import randint

points = 0;

response = requests.get('http://jservice.io/api/clues?category=309').json();

def showPrice():
    print(reponse[0]["Best_Price"]);
    

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def replay():
    replayPrompt = input("Play again? (Y/N)  ")
    if replayPrompt.upper() == "Y":
        print("")
        question();
        
def question():
    global points;
    randomItem = random.randint(0,99);
    value = (response[randomItem]["value"])
    print(("Value: ") + str(value));
    print(response[randomItem]["question"]);
    print("");
    
    correctAnswer = (response[randomItem]["answer"]);
    userAnswer = input();
    correctAnswer = correctAnswer.upper();
    userAnswer = userAnswer.upper();
    correctAnswer = correctAnswer.replace("<I>", '').replace("</I>", '');
    rating = similar(userAnswer, correctAnswer);
    
    if rating > .7:
        print("Correct!");
        print(correctAnswer);
        if type(value) is int:
            points += value;
        else:
            points = points * 2;
    else:
        print("Incorrect!");
        print(correctAnswer);
        if type(value) is int:
            points -= value;
        else:
            points = points // 2;
    print("Total: " + str(points) + " points");
    print("")
    replay();
    
question();