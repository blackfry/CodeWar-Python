__author__ = "Blackfry"



#***********************************************************************
# CODEWARS: Testing 1-2-3
#***********************************************************************

def number(lines):
    return list("%d: %s" % (index, item) for index, item in enumerate(lines, start=1))