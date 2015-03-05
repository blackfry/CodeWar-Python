__author__ = "Blackfry"


#***********************************************************************
# CODEWARS: Boiled Eggs
#***********************************************************************

def cooking_time(eggs):
    capacity = 8
    cook_time = 5
    if eggs % capacity == 0:
        return eggs / capacity * cook_time
    else:
        return (eggs / capacity + 1) * cook_time

print cooking_time(17)
