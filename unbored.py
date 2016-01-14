import itertools

class Bored():
    def __init__(self):
        self.memo = {}

    def smallForm(self, t, n):
        if (t,n) in self.memo:
            pass
        elif t+1 < n:
            self.memo[(t,n)] = 0
        elif n <= 2:
            self.memo[(t,n)] = 1
        elif n == 3:
            self.memo[(t,n)] = pow(2, t+1-n)
        else:
            self.memo[(t,n)] = self.smallForm(t-1,n-1) + self.smallForm(t-1,n) + self.smallForm(t-1, n+1)
        return self.memo[(t,n)]

    def fullForm(self, fullT, n):
        return sum([self.smallForm(t,n) for t in range(n-1,fullT+1)])

def ans(t,n):
    b = Bored()
    #print b.smallForm(t,n)
    return b.smallForm(t,n)
    #return b.fullForm(t,n) % 123454321

#print ans(3,2)
#print ans (7,4)
#print ans (11,4)

print 'so-called answers'
for j in range(2,11):
    for i in range(10):
        print j, j+i-1, ans(j+i-1,j)

#def makeGames(n, t):
#    possibleGames = [[]]
#    for i in range(t-1):
#        possibleGames = (list(x) + [y] for x, y in
#                itertools.product(possibleGames, [-1,0,1]) if sum(x)+y >= 0 and
#                sum(x) + y < n-1) 
#    ans = len(list(l for l in possibleGames if sum(l) == n-2))
#    print n, t, ans
#    return ans
#
#for i in range(10):
#    for j in range(10):
#        makeGames(i+2,i+j+1)
#2 1 1
#2 2 1
#2 3 1
#2 4 1
#2 5 1
#2 6 1
#2 7 1
#2 8 1
#2 9 1
#2 10 1
#3 2 1
#3 3 2
#3 4 4
#3 5 8
#3 6 16
#3 7 32
#3 8 64
#3 9 128
#3 10 256
#3 11 512
#4 3 1
#4 4 3
#4 5 8
#4 6 20
#4 7 49
#4 8 119
#4 9 288
#4 10 696
#4 11 1681
#4 12 4059
#5 4 1
#5 5 4
#5 6 13
#5 7 38
#5 8 106
#5 9 288
#5 10 771
#5 11 2046
#5 12 5401
#5 13 14212
#6 5 1
#6 6 5
#6 7 19
#6 8 63
#6 9 195
#6 10 579
#6 11 1675
#6 12 4763
#6 13 13387
#6 14 37323
#7 6 1
#7 7 6
#7 8 26
#7 9 96
#7 10 325
#7 11 1042
#7 12 3223
#7 13 9724
#7 14 28821
#7 15 84318
#8 7 1
#8 8 7
#8 9 34
#8 10 138
#8 11 506
#8 12 1738
#8 13 5710
#8 14 18174
#8 15 56511
#8 16 172653
#9 8 1
#9 9 8
#9 10 43
#9 11 190
#9 12 749
#9 13 2740
#9 14 9516
#9 15 31824
#9 16 103455
#9 17 329072
#10 9 1
#10 10 9
#10 11 53
#10 12 253
#10 13 1066
#10 14 4134
#10 15 15120
#10 16 52964
#10 17 179534
#10 18 593198

#1   1
#4   8
#8   20
#13  38  (n-1, t-1) + (n, t-1) + n
#
#(n, n+1) => (n-1, n) + n = (n-1, n) + (n, n) + 1
#(n, n+2) => (n-1, n+1) + (n, n+1) + (n+1, n+1)
#(n, n+3) => (n-1, n+2) + (n, n+2) + (n+1, n+2)
#
#general form: (n, t) = (n-1, t-1) + (n, t-1) + (n+1, t-1)
#only I actually want the sum from t=n to T of (n, t)
#also this does not apply to n=3 or less
#also for (t-n) large enough it breaks down
