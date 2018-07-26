#Calculate stats of Fire Emblem: Awakening children
#Currently only the strength stat lol
"""(mother's current stats - mother's class base stats) +
(father's current stats - father's class base stats) +
(child's absolute base stats)
divided by 3, then added to the child's class base stats."""


def inheritance():
    absolute = {
        "kjelle" : [10,6,2,6,5,11,3,3, "Sully"],
        "lucina" : [12,5,1,8,4,13,3,3, "Mother"],
        "owaine" : [10,4,4,5,6,9,6,5, "Lissa"],
        "brady" : [9,6,5,4,2,10,7,4, "Maribelle"],
        "cynthia" : [7,5,2,4,10,17,6,6, "Sumia"],
        "severa" : [8,6,1,7,6,6,6,5, "Cordelia"],
        "gerome" : [13,8,0,4,8,5,5,1, "Cherche"],
        "yarne" : [16,9,1,4,4,13,6,1, "Panne"],
        "noire" : [8,5,3,4,7,10,4,6, "Tharja"],
        "laurent": [10,3,7,7,4,11,4,5, "Miriel"],
        "nah" : [5,3,3,5,6,8,3,3, "Nowi"],
        }
    
    direct = {
        "hp": 0, 
        "strength" : 1, "str" : 1,
        "magic" : 2, "mag" : 2,
        "skill" : 3, "skl" : 3,
        "speed" : 4, "spd" : 4,
        "luck" : 5, "lck" : 5,
        "defense" : 6, "def" : 6,
        "res" : 7, 
        }

    
    stat = input("What stat do you wish to calculate: " ).lower()
    if stat not in direct:
        print("Sorry, '" + stat + "' is not recognized. Please check spelling!")
        inheritanceC()
    
    statIndex = direct[stat]
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
        print(result)
    else:
        print("'" + child + "' is not recognized. Please try again.")
        inheritanceC()
