import itertools

def answer(t,n):
    board = [1] + [0]*(n-1)
    for i in range(t):
        newBoard = [0]*n
        for idx, el in enumerate(board):
            if idx == 0:
                newBoard[0] += el
                newBoard[1] += el
            elif idx + 1 == n:
                newBoard[idx]   += el
            else:
                newBoard[idx-1] += el
                newBoard[idx]   += el
                newBoard[idx+1] += el
            board = newBoard
            #print board
    return newBoard[-1]

print answer(3,2)
print answer(7,4)
print answer(11,4)


def makeGames(n, t):
    possibleGames = [[]]
    for i in range(t-1):
        possibleGames = (list(x) + [y] for x, y in
                itertools.product(possibleGames, [-1,0,1]) if sum(x)+y >= 0 and
                sum(x) + y < n-1) 
    ans = len(list(l for l in possibleGames if sum(l) == n-2))
    #print n, t, ans
    return ans

def allGames(t, n):
    total = 0
    for i in range(n-1, t+1):
        total += makeGames(n, i)
    return (t, n, total)


print allGames(3,2)
print allGames(7,4)
print allGames(11,4)

