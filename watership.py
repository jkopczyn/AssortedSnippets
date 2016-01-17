import copy
import collections

def answer(n):
    start = WarrenState(active={1:n})
    manageStates(start)
    pass

#so it's the problem of largest connected component
#unfortunately, this question is swamped by people 
#asking for answers for this puzzle specifically
#so looking for any approaches is difficult

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

    def merge(self, nudger, nudgee):
        if not nudger in self.active or self.active[nudger] == 0:
            raise ArgumentError
        newState = copy.deepcopy(self)
        possiblePaths = self.active[nudgee]*self.active[nudger]*nudgee
        newWarren = nudger + nudgee
        
        if nudger == nudgee:
            #needs to handle distinct groups of the same size 
            possiblePaths = self.active[nudger]*(nudger-1)
            newState.inactive.setdefault(nudger, 0)
            newState.inactive[nudger] += 1
        elif nudgee in active:
            newState.active.setdefault(newWarren, 0)
            newState.active[newWarren] += 1
            newState.active[nudgee] -= 1
        else:
            newState.inactive.setdefault(newWarren, 0)
            newState.inactive[newWarren] += 1
            newState.inactive[nudgee] -= 1
        newState.active[nudger] -= 1
        newState.multiplicity *= possiblePaths
        deadKeys = [k for k in newState.active.keys() if newState.active[k] <= 0]
	for deadKey in deadKeys:
            del newState.active[deadKey]
        deadKeys = [k for k in newState.inactive.keys() if newState.inactive[k] <= 0]
	for deadKey in deadKeys:
            del newState.inactive[deadKey]
        return newState

def manageStates(initialState):
    queue = collections.OrderedDict([initialState])
    while queue:
        head = queue.pop(last=False)
        for nudger in head.active.keys():
            for nudgee in (head.active.keys() + head.inactive.keys()):
                if nudgee == nudger:
                    pass
