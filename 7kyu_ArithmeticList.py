__author__ = "Blackfry"


#***********************************************************************
# CODEWARS: Arithmetic List!
#***********************************************************************

def seqlist(first, c, l):
    a_seq = []
    for i in range(first, (first + c * l), c):
    	a_seq.append(i)
    return a_seq

def seqlist(first,c,l):
    return range(first,first+l*c,c)


print seqlist(0, 2, 20)