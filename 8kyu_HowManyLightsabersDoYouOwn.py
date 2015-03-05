__author__ = "Blackfry"


#***********************************************************************
# CODEWARS: Ho many lightsabers do you own?
#***********************************************************************
#
#Description:
#
#Inspired by the development team at Vooza, write the function howManyLightsabersDoYouOwn that
#
#accepts the name of a programmer, and
#returns the number of lightsabers owned by that person.
#The only person who owns lightsabers is Zach, by the way. He owns 18, which is an awesome number of lightsabers. Anyone #else owns 0.
#
#No starting help here -- you'll need to know how to write a function that accepts a parameter and returns a value based #on that parameter.



def howManyLightsabersDoYouOwn(name=""):
    return 18 if name == "Zach" else 0