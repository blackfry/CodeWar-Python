__author__ = "Blackfry"



#***********************************************************************
# CODEWARS: Reorganize the weapons!
#***********************************************************************

def identity_weapon(character):

    weapons = {"Laval": "Shado Valious", "Cragger": "Vengdualize", "Lagravis": "Blazeprowlor",
               "Crominus": "Grandorius", "Tormak": "Tygafyre",  "LiElla": "Roarburn"}

    for i in weapons:
        if character in weapons.keys():
            return character + "-" + weapons[character]
        else:
            return "Not a character"

print identity_weapon("Cragger")



def identify_weapon(character):
    weapons = {"Laval": "Shado Valious", "Cragger": "Vengdualize", "Lagravis": "Blazeprowlor",
                "Crominus": "Grandorius", "Tormak": "Tygafyre",  "LiElla": "Roarburn"}
    try:
        newlist = filter(lambda x: character in x, weapons)
        return newlist[0]+"-"+weapons[newlist[0]]
    except:
        return "Not a character"