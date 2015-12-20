import pdb

def answer(words):
    letters = set(c for w in words for c in w)
    #print letters
    orderings = [nextOrdering(words)]
    #print orderings
    listOfWordLists = [words]
    while len(orderings[-1]) < len(letters) and len(listOfWordLists) > 0:
        #pdb.set_trace()
        listOfWordLists = [newList for oldList in 
            listOfWordLists for newList in splitIndex(oldList) if any(newList)]
        for wordList in listOfWordLists:
            ordering = nextOrdering(wordList, orderings[-1])
            #print wordList, orderings, ordering
            if len(ordering) <= 1:
                continue
            elif set(orderings[-1]) - set(ordering):
                orderings.extend(sorted([ordering, orderings.pop()], key=len))
            else:
                orderings[-1] = ordering
    #print orderings
    #pdb.set_trace()
    while len(orderings) > 1:
        orderings = compressOrderings(orderings, orderings[-1])
    return "".join(orderings[-1])

def splitIndex(words):
    listOfOrderings = []
    ordering = []
    firstLetter = False
    for w in (w for w in words if len(w) > 1):
        firstLetter = firstLetter or w[0]
        if w[0] == firstLetter:
            ordering.append(w[1:])
            continue
        else:
            listOfOrderings.append(ordering)
            firstLetter = w[0]
            ordering = [w[1:]]
    if len(ordering) > 0:
        listOfOrderings.append(ordering)
    listOfOrderings.sort(key=lambda l: -len(l))
    return listOfOrderings

def nextOrdering(words, priorOrder=[]):
    firstChars = [w[0] for w in words if len(w) >= 1]
    return findImplicitOrder(firstChars, priorOrder)

def findImplicitOrder(chars, priorOrder=[]):
    explicitOrder = []
    newCharsSet = set()
    newCharsOrder = []
    priorSet = set(priorOrder)
    for c in (c for c in chars if c not in newCharsSet):
        newCharsSet.add(c)
        newCharsOrder.append(c)
    if not newCharsSet & priorSet:
        return newCharsOrder
    for c in newCharsOrder:
        try:
            idx = priorOrder.index(c)
            before = priorOrder[0:idx]
        except ValueError:
            before = []
        explicitOrder.extend([d for d in before if d in (set(before) - set(explicitOrder))])
        explicitOrder.append(c)
    try:
        after = priorOrder[idx+1:]
    except NameError: #never pulled from priorOrder, idx undefined
        after = [] #this means the new order hs no overlap
    explicitOrder.extend(after)
    return explicitOrder

def compressOrderings(orderings, newOrdering):
        compressed = []
        for ordering in orderings:
            if not (set(ordering) & set(newOrdering)):
                compressed.append(ordering)
            betterOrdering = nextOrdering(ordering, newOrdering)
            if not (set(newOrdering) - set(betterOrdering)):
                newOrdering = betterOrdering
            else:
                compressed.append(betterOrdering)
        compressed.append(newOrdering)
        return compressed

print answer(["adc", "bdc", "bdd", "be", "ccc"])
print answer(["adc", "bac", "bbd", "bd", "ccc", "ccd"])
