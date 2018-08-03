#Calculate a base stat of Fire Emblem: Awakening children on their recruitment
#Version1.3
#Chloe Xie 2018
#AI4ALL
"""(mother's current stats - mother's class base stats) +
(father's current stats - father's class base stats) +
(child's absolute base stats)
divided by 3, then added to the child's class base stats."""

#implementing a global list. In real world, global lists have security issues

absolute = {
    "brady" : [9,6,5,4,2,10,7,4, "Maribelle"],
    "cynthia" : [7,5,2,4,10,17,6,6, "Sumia"],
    "gerome" : [13,8,0,4,8,5,5,1, "Cherche"],
    "kjelle" : [10,6,2,6,5,11,3,3, "Sully"],
    "laurent": [10,3,7,7,4,11,4,5, "Miriel"],
    "lucina" : [12,5,1,8,4,13,3,3, "Mother"],
    "nah" : [5,3,3,5,6,8,3,3, "Nowi"],
    "noire" : [8,5,3,4,7,10,4,6, "Tharja"],
    "owain" : [10,4,4,5,6,9,6,5, "Lissa"],
    "severa" : [8,6,1,7,6,6,6,5, "Cordelia"],
    "yarne" : [16,9,1,4,4,13,6,1, "Panne"],   
    }

statDict = {
    "hp": 0, 
    "strength" : 1, "str" : 1,
    "magic" : 2, "mag" : 2,
    "skill" : 3, "skl" : 3,
    "speed" : 4, "spd" : 4,
    "luck" : 5, "lck" : 5,
    "defense" : 6, "def" : 6,
    "res" : 7, 
    }
    
def inheritance():
    stat = input("What stat do you wish to calculate: " ).lower()
    if stat in statDict:
        statIndex = statDict[stat]
        child1(statIndex, stat)
    else:
        print(stat + " is unrecognized. Try again.")
        inheritance()


def child1(statIndex, stat):
    child0 = input("Whose " + stat + " stat will we calculate?: ")
    child = child0.lower()

    if child in absolute:
        bStatM = int(input(absolute[child][8] + "'s class base " + stat + ": " ))
            
        cStatM = int(input(absolute[child][8] + "'s current "  + stat + ": " ))
     
        bStatF = int(input("Father's class base " + stat +": " ))

        cStatF = int(input("Father's current " + stat + ": " ))

        cStatc = int(input(child0 + "'s class base " + stat + ": " ))

        result = int(((cStatF - bStatF) + (cStatM - bStatM))
                         / 3 + absolute[child][statIndex])
        print("Resulting " + stat + " stat: " + str(result))
    
    else:
        print("'" + child + "' is not recognized. Please try again.")
        child1(statIndex, stat)

        
def dream():
    x = 13
    y = 17.0
    print(isinstance(x, int))
    print(isinstance(y, int))
    
