__author__ = "Blackfry"



#***********************************************************************
# CODEWARS: Replace multiples with string (FIZZBUZZ)
#***********************************************************************

def get_number(number):
    fizzbuzz = ""
    if isinstance(number, int):
        if (number % 5 == 0) and (number % 3 == 0):
            fizzbuzz = "BOTH"
        elif number % 3 == 0:
            fizzbuzz = "THREE"
        elif number % 5 == 0:
            fizzbuzz = "FIVE"
        else:
            fizzbuzz = number
        return fizzbuzz
    else:
        return "Not a valid integer."


def getNumberRange(first, last):
    a_list = []
    if isinstance(first or last, int):
        if first < last:
            for i in range(first, last + 1):
                a_list.append(get_number(i))
            return a_list
        else:
            for i in range(first, last - 1, -1):
                a_list.append(get_number(i))
            return a_list
    else:
        return "Integer/s not valid."