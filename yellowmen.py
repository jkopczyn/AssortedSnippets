class LetterNode:
    def __init__(self, letter):
        self.letter = letter
        self.predecessors = set()
        self.followers = set()
    def simplify(self):
        ancestors = self.predecessors.copy()
        queue = list(ancestors)
        for letter in queue:
            if letter in ancestors:
                continue
            else:
                ancestors.add(letter)
                queue.extend(letter.predecessors)
        descendants = self.followers.copy()
        queue = list(descendants)
        for child in queue:
            child.predecessors -= ancestors
            queue.extend(child.followers)
            descendants.add(child)
        for parent in ancestors:
            parent.followers -= descendants
    def singlePath(self):
        if len(self.followers) > 1 or len(self.predecessors) > 1:
            return False
        elif len(self.predecessors) > 0:
            return (x for x in self.predecessors).next().singlePath()
        else:
            string = ""
            head = self
            while True:
                string += head.letter
                if len(head.followers) > 1:
                    return False
                elif len(head.followers) == 0:
                    return string
                else:
                    head = list(head.followers)[0]

def answer(words):
    letters = set(c for w in words for c in w)
    letterNodes = {c : LetterNode(c) for c in letters}
    queueOfWordlists = [words]
    for wl in queueOfWordlists:
        addToGraph(wl, letterNodes)
        queueOfWordlists.extend(suffixWordlists(wl))
    for node in letterNodes.values():
        node.simplify()
    for node in letterNodes.values():
        order = node.singlePath()
        if order and len(order) == len(letters):
            return order
    return False


def addToGraph(words, letterNodes):
    firstCharsSet = set()
    firstCharsOrder = []
    for c in (w[0] for w in words if len(w) and w[0] not in firstCharsSet):
        letterNodes[c].predecessors |= set(letterNodes[d] for d in firstCharsSet)
        for parent in letterNodes[c].predecessors:
            parent.followers.add(letterNodes[c])
        firstCharsSet.add(c)

def suffixWordlists(words):
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
    return listOfOrderings

print answer(["adc", "bdc", "bdd", "be", "ccc"])
print answer(["adc", "bac", "bbd", "bd", "ccc", "ccd"])
