__author__ = "Blackfry"



#***********************************************************************
# CODEWARS: Disemvowel Trolls
#***********************************************************************

def disemvowel(string):
    new_string = ""
    vowels = "aeiou"
    for i in string:
        if i.lower() not in vowels:
            new_string += i
    return new_string