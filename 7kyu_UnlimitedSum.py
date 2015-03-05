__author__ = "Blackfry"


#***********************************************************************
# CODEWARS: Unlimited Sum
#***********************************************************************

def sum(*args):
    total = 0
    for i in args:
        if isinstance(i, int):
            total += i
    return total
