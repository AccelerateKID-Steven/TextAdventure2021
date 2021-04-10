#Text Adventure Game
#Steven Kalis
#11/14/2020

#What a Game Needs
#1) Player - could be one, or more than one
#2) Enemies - could be one, or more
#3) Choices - ex: where to go, what to choose, what to be
#4) Outcomes dependent on those choices
#5) Setting
import random 

myChoice = ""
enemy = ""
#Nested Dictionaries
gameInfo = {

    #character values that change/update with decisions
    "name":" ",
    "class":" ",
    "skills":[ ],
    "randomAlly": "",
    #Dictionaries of constant variables
    "swordAttributes" : {
        #keys: values
        "name": "sword",
        "maxhp": 75,
        "maxmana": 50,
        "ability": "steadfast",# when below 20% mana, gains 15% mana over time for 2 rounds
        "swordChoice" : ["Slash","Weaken"],
        "hero": " ",
        "weakness": "bow"
        },
    "bowAttributes" : {
        #keys: values
        "name": "bow",
        "maxhp": 60,
        "maxmana": 70,
        "ability": "far-reach",#consecutive moves increase the abilitys power
        "bowChoice" : ["Snipe", "Slow"],
        "hero": " ",
        "weakness": "staff"
        },

    "staffAttributes" : {
        #keys: values
        "name": "staff",
        "maxhp": 45,
        "maxmana": 95,
        "ability": "second-grace",#heals will heal 15% more, and heal up to 20% more if used when hit
        "staffChoice" : ["Fireball", "Heal"],
        "hero": " ",
        "weakness": "sword"
      },
    "skillDictionary":{
        "slash": [gameInfo["name"] + " slashes " + enemy + "for 15 DMG!",-15],
        "snipe": [gameInfo["name"] + " shoots an arrow at " + enemy + "for 20 DMG!",-20],
        "fireball": [gameInfo["name"] + " summons a fireball towards " + enemy + "for 25 DMG!",-20],
        "weaken": [gameInfo["name"] + " weakens " + enemy + "for 10 DMG!",-10],
        "slow": [gameInfo["name"] + " slows down " + enemy + "for 5 DMG!",-5],
        "heal": [gameInfo["name"] + " heals  for 20 HP!",20]
    }
     
}#end of gameInfo dictionary

#the function that starts off the game
def gameStart():
    correct = False
    print("Welcome to\n\nAdventure Quest Worlds\n----------------\n")
    myChoice = input("Tell me your character's name: ")
    gameInfo["name"] = myChoice

    #choose class
    while correct == False:

        myChoice = input("There are three different classes in the\nAdventure Quest Worlds" +
                    "\nWarrior\n------------\n" +
                    "\nArcher\n------------\n"  +
                    "\nMage\n------------\nWhich one will you choose? ")
        
        # if they chose Warrior, break out of loop
        if myChoice.lower() == "warrior":
            #already made key with a new value
            gameInfo["class"] = "warrior"
            #new key with a constant value at the start
            gameInfo["skills"] = gameInfo["swordAttributes"]["swordChoice"]
            gameInfo["hp"] = gameInfo["swordAttributes"]["maxhp"]
            gameInfo["mp"] = gameInfo["swordAttributes"]["maxmana"]
            correct = True

        # if they chose Archer, break out of loop
        elif myChoice.lower() == "archer":
            gameInfo["class"] = "archer"
            gameInfo["skills"] = gameInfo["bowAttributes"]["bowChoice"]
            gameInfo["hp"] = gameInfo["bowAttributes"]["maxhp"]
            gameInfo["mp"] = gameInfo["bowAttributes"]["maxmana"]
            correct = True

        #if they chose Mage, break out of loop
        elif myChoice.lower() == "mage":
            gameInfo["class"] = "mage"
            gameInfo["skills"] = gameInfo["staffAttributes"]["staffChoice"]
            gameInfo["hp"] = gameInfo["staffAttributes"]["maxhp"]
            gameInfo["mp"] = gameInfo["staffAttributes"]["maxmana"]
            correct = True

        #if they didn't type any of that, show an error message
        else:
            print("ERROR - Input not detected")
    
    print("You have chosen " + gameInfo["class"] + "!")

#variables to use: HP, MP, EnemyType, EnemyHP, EnemyMP
def startFight(enemy):
    #Core Gameplay that depends on the type of game you're making!
    correct = False
    #inform the user that a fight has started and give them a choice on what to do
    print("A fight has broken out with the " + enemy + "")
    if(enemy == "bandit"):
        banditChoice = gameInfo["swordAttributes"]["swordChoice"]
        banditHP = gameInfo["swordAttributes"]["maxhp"]
        banditMP = gameInfo["swordAttributes"]["maxmana"]
    while(banditHP >= 1 and gameInfo["hp"] >= 1):
        while (not correct):
            selection = input("\n What will you do?\nSkill\nCheck Stats\nRun")
            if selection.lower() == "skill":
                #show all skills usable
                print("Which skill will you use")
                for skill in gameInfo["skills"]:
                    print(skill + "\n")
                skillChoice = input("?\n")
                #create a big ol' loop to do something
                #depending on what i do
                #TODO: create loop for skill and do skill depending on choice
            

            elif selection.lower() == "check stats":
                #view your stats and the enemies stats
                bob=1
                
            else:
                print("Error - Input not detected")

        #loop through this until one is defeated

#Next function to make :actionStart
def actionStart(action):
    correct = False
    
    while(not correct):#loops will run as long as it has a boolean value of true
        #not is a boolean keyword that inverses the boolean
        #if statement
        if action.lower() == "left":
            #If the player goes left for the first action 
            correct = True
            #runs into a bandit
            startFight("bandit")


        elif action.lower() == "straight":
            #If the player goes straight for the first action
            correct = True
            #gets punched, loses health
            #lowering a stat/increasing a stat depending on a situation
            print("On your way out of the village you get punched in the face\n you lose 10HP")
            gameInfo["hp"] = gameInfo["hp"] - 10
            #maybe get something out of it to make it worth

        elif action.lower() == "right":
            #If the player goes right for the first action
            correct = True
            #Gain a skill
            #add a new item into the array from the dictionary
            if gameInfo["class"] == "warrior":
                print("Heading towards a lake, you run into a herbalist who shows you how to craft a potion of health!")
                print("However, this potion can only be used once in a fight")
                gameInfo["skills"].append("Health Potion")
            elif gameInfo["class"] == "archer":
                print("Heading towards a lake, you run into a herbalist who shows you how to craft a potion of mana!")
                print("However, this potion can only be used once in a fight")
                gameInfo["skills"].append("Mana Potion")
            else:
                print("Heading towards a lake, you run into a fellow wizard who shows you how to make \nyour" + 
                        "spells stronger for a period of time!")
                gameInfo["skills"].append("Buff")

            #Add new skill
            print("You have learned the skill " + gameInfo["skills"][2] + "!")
            



        #more elif statments to come...
        else:
            action = input("Error - Try again:")
            correct = False
    


#beginning of game code starts here
gameStart()
print("-----------------\n")
action = input("Greetings " + gameInfo["name"] +", you have started out in the town of\nBeginnersville. " +
                "There is a fork in the road, will you go:\nLeft,\nStraight\nor Right?")
#call said function here:
actionStart(action)
#if we didn't go left, fight the bandit
if not (action.lower == "left"):
    startFight("bandit")








