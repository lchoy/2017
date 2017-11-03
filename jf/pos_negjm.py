"""Given 2 int values, return True if one is negative and one is positive.

Except if the parameter "negative" is True, then return True only if both are negative.

pos_neg(1, -1, False) => True
pos_neg(-1, 1, False) => True
pos_neg(-4, -5, True) => True
"""


def pos_neg(a, b, negative):

    if negative == True :
        if a < 0:
            if b < 0:
             return True

    if a*b >= 0:
        return False

    if a*b <= 0:
      return True






print pos_neg(1, -1, False)
print pos_neg(-1, 1, False)
print pos_neg(-4, -5, True)
