__author__ = "Blackfry"



#***********************************************************************
# CODEWARS: Check for prime numbers
#***********************************************************************

def is_prime(n):
    x = 0
    if isinstance(n, int) and n > 2:
        for i in range(2, n - 1):
            if n % i == 0:
                x += 1
                break
        return True if x == 0 else False
    else:
        return False