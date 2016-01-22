import copy
import collections
import fractions

#so it's the problem of largest connected component
#unfortunately, searching for anything like this 
#question is swamped by people asking for answers 
#for this puzzle specifically, so looking for
#fruitful potential approaches is difficult

#one approach: sort rabbits/nodes into unwarrened,
#has-nudged, and warrened-but-has-not-nudged
#for each warren/component, track how many 
#of the rabbits are yet to nudge
#this could be useful for memoization
#but there ought to be a better way
#wait, there will never be a warren with more than 
#one nudge available. that simplifies things

#so states should have parent lists, each with a number associated.
#when everything with X+1 active groups is out of the queue, states with X
#active groups can be calculated explicitly and X+1 groups wiped

def answer(n):
    start = StateNode(active={1:n}, copies=1)
    tiers = collections.defaultdict(list)
    allSeen = set([start])
    queue = collections.deque([start])
    tiers[n].append(start)
    size = n
    #import pdb; pdb.set_trace()
    while len(queue) > 0:
        head = queue.popleft()
        #print '\n\nhead:', head.active, head.inactive, 'copies:', head.copies
        #print "headSize:", sum(head.active.values()), "size:", size, '\n\n'
        if sum(head.active.values()) < size:
            calcAndClean(tiers, size-1)
            #print 'size drop from', size, 'to', sum(head.active.values()), head.active
            size = sum(head.active.values())
        for succ, val in head.successors():
            succ.parents[head] = val
            if succ in allSeen:
                tiers[size-1][(tiers[size-1].index(succ))].parents[head] = val
            else:
                tiers[size-1].append(succ)
                queue.append(succ)
                allSeen.add(succ)
    calcAndClean(tiers, 0)
    #print "final tiers:", tiers
    return renderOutput(tiers[0])

def renderOutput(nodes):
    #print "nodes:", nodes
    cases = sum([node.copies for node in nodes])
    total = sum([node.copies * max(node.inactive.keys()) for node in nodes])
    divideBy = fractions.gcd(cases, total)
    #print total, cases, divideBy
    return str(total/divideBy)+"/"+str(cases/divideBy)

def calcAndClean(tiers, size):
    #print 'calcAndClean', tiers, size
    if not tiers[size+1]:
        return
    parentHash = set(parent for parent in tiers[size+1])
    #import pdb; pdb.set_trace()
    for node in tiers[size]:
        #print 'calcNode', node, node.parents
        node.copies = sum(parent.copies * multiple for parent, multiple in node.parents.items())
    tiers.pop(size+1, None)

#things I need: parents (hash from Node to multiplicity), successors (list), copies (starts as None)
#StateNodes need to be hashable; active and inactive should be sufficient for
#this purpose

class StateNode:
    def __init__(self, active=(), inactive=(), copies=None, parents={}):
        self.active = collections.defaultdict(int, active)
        self.inactive = collections.defaultdict(int, inactive)
        self.parents = parents
        self.copies = copies

    def warrens(self):
        return (tuple(self.active.items()), tuple(self.inactive.items()))

    def __copy__(self):
        return StateNode(self.active, self.inactive, self.copies, dict(self.parents))

    def __repr__(self):
        return "".join(str(el) for el in ("active: ",self.active," inactive: ",
            self.inactive," copies: ",self.copies," parents: ",self.parents))

    def __hash__(self):
        return hash(self.warrens())

    def __eq__(self, other):
        return self.warrens() == other.warrens()

    def successors(self):
        newStates = []
        removeZeroes(self.active)
        removeZeroes(self.inactive)
        activeSizes = frozenset(self.active.keys())
        inactiveSizes = frozenset(self.inactive.keys())
        for size in activeSizes:
            if size > 1:
                newActive = copy.deepcopy(self.active)
                newInactive = copy.deepcopy(self.inactive)
                newActive[size]   -= 1
                newInactive[size] += 1
                StateNode.addPrepped(newStates, newActive, newInactive, size-1)
            for secondSize in activeSizes:
                if secondSize == size and self.active[size] <= 1:
                    continue
                newActive = copy.deepcopy(self.active)
                newActive[size] -= 1
                newActive[secondSize] -= 1
                newActive[size + secondSize] += 1
                permutations = self.active[secondSize] * self.active[size]
                if size == secondSize:
                    permutations -= self.active[size]
                StateNode.addPrepped(newStates, newActive, self.inactive, secondSize * permutations)
            for secondSize in inactiveSizes:
                newActive = copy.deepcopy(self.active)
                newInactive = copy.deepcopy(self.inactive)
                newActive[size] -= 1
                newInactive[secondSize] -= 1
                newInactive[size + secondSize] += 1
                StateNode.addPrepped(newStates, newActive, newInactive, 
                    secondSize * self.inactive[secondSize] * self.active[size])
        return newStates

    @classmethod
    def addPrepped(cls, stateList, activeHash, inactiveHash, multiplicity):
        stateList.append((StateNode(active=activeHash, inactive=inactiveHash), multiplicity))
        return stateList

def removeZeroes(dictionary):
    for key in [k for k in dictionary.keys() if dictionary[k] == 0]:
        del dictionary[key]

print answer(2)
print answer(3)
print answer(4)
print answer(5)
print answer(6)
print answer(7)
print answer(8)
print answer(9)
print answer(10)
print answer(11)
print answer(12)
