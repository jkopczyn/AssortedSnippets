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

class WarrenState():
    def __init__(self, active={}, inactive={}, multiplicity=1):
        #active and inactive store group sizes as keys,
        #and number of groups present that size as values
        self.active = collections.Counter(active)
        self.inactive = collections.Counter(inactive)
        self.multiplicity = multiplicity
    def __copy__(self):
        #technically not a proper shallow copy. technically.
        return WarrenState(self.active.copy(), self.inactive.copy(), self.multiplicity)
    def copy(self):
        return copy.copy(self)

    def __deepcopy__(self,memo):
        act = copy.deepcopy(self.active, memo)
        inact = copy.deepcopy(self.inactive, memo)
        return WarrenState(act, inact, self.multiplicity)
    def deepcopy(self):
        return copy.deepcopy(self)

    def __eq__(self, other):
        return self.active == other.active and self.inactive == other.inactive
        
    def __hash__(self): #is 17 just a convenient prime, or was there some other reason?
        return 17*(self.active.hash()+17*(self.inactive.hash()+17*self.mutiplicity))

    def successors(self):
        newStates = []
        self.active += Counter()
        self.inactive += Counter()
        for size in self.active.most_common():
            if size > 1:
                newState = self.deepcopy()
                newState.multiplicity *= size-1
                newState.active[size] -= 1
                newState.inactive[size] += 1
                newStates.append(newState)
            for secondSize in self.active.most_common():
                if secondSize == size and self.active[size] <= 1:
                    continue
                newState = self.deepcopy()
                newState.multiplicity *= secondSize * self.active[secondSize] * self.active[size]
                newState.active[size] -= 1
                newState.active[secondSize] -= 1
                newState.active[size + secondSize] += 1
                newStates.append(newState)
            for secondSize in self.inactive.most_common():
                newState = self.deepcopy()
                newState.multiplicity *= secondSize * self.inactive[secondSize] * self.active[size]
                newState.active[size] -= 1
                newState.inactive[secondSize] -= 1
                newState.inactive[size + secondSize] += 1
                newStates.append(newState)
        return newStates

    def freeze(self):
        return ((frozenset(self.active.items()),
                frozenset(self.inactive.items())), self.multiplicity)


#so states should have parent lists, each with a number associated.
#when everything with X+1 active groups is out of the queue, states with X
#active groups can be calculated explicitly and X+1 groups wiped

def tentative(n):
    start = StateNode(active={1:n}, copies=1)
    tiers = collections.defaultdict(list,[(n,start)])
    queue = collections.deque(start)
    size = n
    while queue:
        head = queue.popLeft()
        if len(head.active) < size:
            calcAndClean(tiers, size)
            size = len(head.active)
        if head in tiers[size]:
            continue
        for succ, val in head.successors():
            extant = next(i for i, s in enumerate(tiers[size-1]) if s.warrens() ==
                    succ.warrens(), None)
            if extant:
                extant.parents[head] = succ.parents[head]
            else:
                tiers[size-1].append(succ)
                queue.append(succ)
    calcAndClean(tiers, 0)
    cases = sum([node.copies for node in tiers[0]])
    total = sum([node.copies * max(node.inactive.keys()) for node in tiers[0]])
    divideBy = fractions.gcd(cases, total)
    return str(total/divideBy)+"/"+str(cases/divideBy)

def calcAndClean(tiers, size):
    for node in tiers[size]:
       node.copies = sum(parent.copies * multiple for parent, multiple in node.parents())
    del tiers[size+1]

#things I need: parents (hash from Node to multiplicity), successors (list), copies (starts as None)
#StateNodes need to be hashable; active and inactive should be sufficient for
#this purpose

class StateNode:
    def __init__(self, active=(), inactive=(), parents={}, copies=None):
        self.active = dict(active)
        self.inactive = dict(inactive)
        self.parents = parents
        self.copies = copies
    
    def warrens(self):
        return (tuple(self.active.items()), tuple(self.inactive.items()))

    def __hash__(self):
        return hash(self.warrens())

    def __eq__(self, other):
        return self.warrens() == other.warrens()

    def successors(self):
        raise IHaveNoIdeaWhatImDoingException
