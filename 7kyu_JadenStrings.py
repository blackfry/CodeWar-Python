#***********************************************************************
# CODEWARS: Jaden Casing Strings
#***********************************************************************


def toJadenCase(string):
    newlist = []
    stringlist = string.split()
    for word in stringlist:
        tempstring = ""
        for letter in word:
            if len(tempstring) == 0:
                tempstring += letter.upper()
            else:
                tempstring += letter
        newlist.append(tempstring)
    return " ".join(newlist)