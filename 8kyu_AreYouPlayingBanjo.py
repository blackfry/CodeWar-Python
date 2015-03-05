__author__ = "Blackfry"



#***********************************************************************
# CODEWARS: Are You Playing Banjo?
#***********************************************************************
#
#Description:
#
#Create a function which answers the question "Are you playing Banjo?". If your name starts with the letter "R" or lower #case "r", you are playing Banjo!
#
#The function takes a name as its only argument, and returns one of the following strings:
#
#"[name] plays banjo"
#"[name] does not play banjo"
#Names given are always valid strings.



def areYouPlayingBanjo(name):
    return '%s %s' %(name, "plays banjo" if name[0].lower() == "r" else "does not play banjo")