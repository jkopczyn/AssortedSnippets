import itertools
def answer(x, y, z):
    possibles = list(set(n for n in itertools.permutations([x,y,z]) if validDate(*n)))
    print possibles
    if len(possibles) == 1:
        return "{x!s:0>2}/{y!s:0>2}/{z!s:0>2}".format(**locals())
    else:
        return "Ambiguous"

def validMonth(n):
    return 1 <= n and n <= 12

def validDay(n, month=1):
    if month in [9, 4, 6, 11]:
        return 1 <= n and n <= 30
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 1 <= n and n <= 31
    elif month == 2:
        return 1 <= n and n <= 28
    else:
        return False

def  validDate(x,y,z):
    return validMonth(x) and validDay(y,x)
