import copy
import itertools

def answer(minions):
    minimumScore = sum(m[0] for m in minions)
    bestOrder = []
    for order in itertools.permutations(range(len(minions))):
        minOrder = [minions[idx] for idx in order]
	#print "order: ", order
        candScore = leftScore(minOrder, minimumScore)
        if candScore:
	    #print "best order: ", order, "best score: ", candScore
            minimumScore = candScore
            bestOrder = order
    return bestOrder

def leftScore(minionOrder, minimum=0):
    minionOrder = copy.copy(minionOrder)
    score = 0.0
    #numerator, denominator
    failureChance = [1,1]
    for m in minionOrder:
        if minionOrder[-1] == m:
            score += (1.0 * failureChance[0] * m[0])/failureChance[1]
        else:
            score += (1.0 * failureChance[0] * m[0])/failureChance[1]
            failureChance[0] *= (m[2]-m[1])
            failureChance[1] *= m[2]
	#print "m: ", m, "score: ", score
        if minimum and score >= minimum:
            return False
    return score


print answer([[5, 1, 5], [10, 1, 2]])
t = [[390, 185, 624], [686, 351, 947], [276, 1023, 1024], [199, 148, 250]]
print answer(t)
t += [[5, 1, 5], [10, 1, 2]]
print answer(t)

def expected(minion):
    expectedTriesPerSuccess = (minion[2]*1.0)/minion[1]
    expectedTimeAdded = minion[0] * expectedTriesPerSuccess
    return expectedTimeAdded
    #heh this is very frequentist
    

import copy
import itertools

def answer(minions):
    minimumScore = sum(m[0] for m in minions)
    bestOrder = []
    for order in itertools.permutations(range(len(minions))):
        minOrder = [minions[idx] for idx in order]
	#print "order: ", order
        candScore = leftScore(minOrder, minimumScore)
        if candScore:
	    #print "best order: ", order, "best score: ", candScore
            minimumScore = candScore
            bestOrder = order
    return bestOrder

def leftScore(minionOrder, minimum):
    minionOrder = copy.copy(minionOrder)
    score = 0.0
    #numerator, denominator
    failureChance = [1,1]
    for m in minionOrder:
        if minionOrder[-1] == m:
            score += (1.0 * failureChance[0] * m[0])/failureChance[1]
        else:
            score += (1.0 * failureChance[0] * m[0])/failureChance[1]
            failureChance[0] *= (m[2]-m[1])
            failureChance[1] *= m[2]
	#print "m: ", m, "score: ", score
        if score >= minimum:
            return False
    return score

