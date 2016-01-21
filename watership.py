import copy
import collections
import fractions

def answer(n):
    start = WarrenState(active={1:n})
    manageStates(start)
    pass

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

def tentative(n):
    start = StateNode(active={1:n}, copies=1)
    tiers = collections.defaultdict(list,[])
    queue = collections.deque([start])
    size = n
    while len(queue) > 0:
        head = queue.popleft()
        print '\n\nhead:', head.active, head.inactive, 'copies:', head.copies
        print "headSize:", sum(head.active.values()), "size:", size, '\n\n'
        if sum(head.active.values()) < size:
            calcAndClean(tiers, size)
            print 'size drop from', size, 'to', sum(head.active.values()), head.active
            size = sum(head.active.values())
        for succ, val in head.successors():
            extant = next((i for i, s in enumerate(tiers[size-1]) if s.warrens() == succ), None)
            print 'extant?', extant, succ
            if extant:
                extant.parents[head.warrens()] = val
            else:
                succNode = StateNode(*succ, parents={head.warrens(): val} )
                if succNode in tiers[size-1]:
                    print 'already here', succNode, succ, tiers[size-1]
                    continue
                tiers[size-1].append(succNode)
                queue.append(succNode)
    calcAndClean(tiers, 0)
    print "final tiers:", tiers
    return renderOutput(tiers[0])

def renderOutput(nodes):
    print "nodes:", nodes
    cases = sum([node.copies for node in nodes])
    total = sum([node.copies * max(node.inactive.keys()) for node in nodes])
    divideBy = fractions.gcd(cases, total)
    print total, cases, divideBy
    return str(total/divideBy)+"/"+str(cases/divideBy)

def calcAndClean(tiers, size):
    print 'calcAndClean', tiers, size
    for node in tiers[size]:
        print 'calcNode', node.warrens(), node.parents
        node.copies = sum(parent.copies * multiple for parent, multiple in node.parents.items())
    #tiers.pop(size+1, None)

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
                StateNode.addPrepped(newStates, newActive, self.inactive, 
                    secondSize * self.active[secondSize] * self.active[size])
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
        stateList.append(((activeHash.items(), inactiveHash.items()), multiplicity))
        return

def removeZeroes(dictionary):
    for key in [k for k in dictionary.keys() if dictionary[k] == 0]:
        del dictionary[key]

print tentative(2)
