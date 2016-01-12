import math
import itertools
import copy

def leftHeadcount(arr):
    if not arr:
        return 0
    max = arr[0]-1
    count = 0
    for el in arr:
        if el > max:
            max = el
            count += 1
    return count

def rightHeadcount(arr):
    brr = copy.copy(list(arr))
    brr.reverse()
    return leftHeadcount(brr)

def summary(n):
    print None
    print None
    print None
    v = [(leftHeadcount(p), rightHeadcount(list(p))) for p in
        itertools.permutations(list(range(1,n+1)))]
    v.sort()
    v2 = [(k, len(list(g))) for k, g in itertools.groupby(v)]
    v2.sort(key=lambda x: (x[0][0]+x[0][1], x[0][0]))
    for el in v2:
        print el

#summary(1)
#summary(2)
#summary(3)
#summary(4)
#summary(5)
#summary(6)
#summary(7)
#summary(8)
#summary(9)


#5: 1, 6, 11, 6
#6: 1, 10, 35, 50, 24
#7: 1, 15, 85, 225, 274, 120
#8: 1, 21, 175, 735, 1624, 1764, 720
#
#n rabbits, l seen from the left, r from the right#
#
#(Pascal row 0 is "1", row 1 is "1 1", row 2 is "1 2 1", etc.)
#
#entry is Pascal(row: l+r-2, col: l) * T(row: n-1, col: n-(l+r)+2)
#Pascal(l+r-2, l) is choose((l-1)+(r-1), (l-1))
#T(n,k) = abs(Stirling number(n, n+1-k)) = 
#so 
#T(row: n-1, col: n-(l+r)+2) = abs(Stirling(n-1, (n-1)-(n-(l+r)+2)+1))
#	=abs(Stirling(n-1, l+r-2))

def pascal(n,k):
    return math.factorial(n)/(math.factorial(n-k) * math.factorial(k))

class Stirling():
    def __init__(self):
        self.memo = {(0,0): 1}
        
    def s(self,n,k):
        if (n,k) in self.memo:
            return self.memo[(n,k)]
        elif n == 0 or k ==0:
            self.memo[(n,k)] = 0
            return 0
        self.memo[(n,k)] = (n-1) * self.s(n-1,k) + self.s(n-1,k-1)
        #print self.memo[(n,k)]
        return self.memo[(n,k)]
        
def answer(x, y, n):
    l = x-1
    r = y-1
    m = n-1
    s = Stirling()
    return str(pascal(l+r,l) * s.s(m,l+r))
