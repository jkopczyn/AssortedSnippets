import itertools

def answer(str_S):
    target = int(str_S)
    R = Recurrence()
    i = 1
    highExp = R.logSearch(target)
    return str(R.fineSearch(target, highExp))

#closed form?
#a^n+b^n+n?
#a^(n/2)+b^(n/2)+n/2 + a^(n/2-1)+b^(n/2-1)+n/2 + n
    
class Recurrence:
    def __init__(self):
        self.store = {0: 1, 1: 1, 2: 2}

    def f(self, n):

        queue = [n]
        while queue:
            head = queue.pop()
            if head in self.store:
                pass
            elif head%2:
                m = (head-1)/2
                if m in self.store and m-1 in self.store:
                    self.store[head] = self.store[m] + self.store[m-1] + 1
                else:
                    queue.append(head)
                    if m not in self.store:
                        queue.append(m)
                    if m-1 not in self.store:
                        queue.append(m-1)
            else:
                m = head/2
                if m in self.store and m+1 in self.store:
                    self.store[head] = self.store[m] + self.store[m+1] + m
                else:
                    queue.append(head)
                    if m not in self.store:
                        queue.append(m)
                    if m+1 not in self.store:
                        queue.append(m+1)
        return self.store[n]
    
    def logSearch(self,target):
        if target <= 1:
            return 0
        elif target == 2:
            return 1
        elif target <= 7:
            return 2
        exp = 2
        while self.f(pow(2,exp)) < target:
            exp += 1
        return exp

    def fineSearch(self, target, exp):
        if target < 15:
            early = {1: 1, 2: 2, 3: 3, 7: 4, 4: 5, 13: 6, 6: 7}
            if target in early:
                return early[target]
            else:
                return None
        oddSolution = None
        evenSolution = None
        print target, exp

        lowBound  = pow(2, exp-2)-1
        highBound = pow(2, exp  )+1
        #search in odd first; if it's in odd, that's later
        while highBound - 2 > lowBound:
            diff = highBound - lowBound
            trial = lowBound + diff/2
            if not trial % 2:
                trial += 1
            print trial
            if self.f(trial) > target:
                highBound = trial
            elif self.f(trial) < target:
                lowBound = trial
            elif self.f(trial) == target:
                while self.f(trial+2) == target:
                    trial = trial + 2
                oddSolution = trial
                break
        #proceed to even
        lowBound  = pow(2, exp-2)-2
        highBound = pow(2, exp)+2
        while highBound - 2 > lowBound:
            diff = highBound - lowBound
            trial = lowBound + diff/2
            if trial % 2:
                trial += 1
            print trial
            if self.f(trial) > target:
                highBound = trial
            elif self.f(trial) < target:
                lowBound = trial
            elif self.f(trial) == target:
                while self.f(trial+2) == target:
                    trial = trial + 2
                evenSolution = trial
                break
        return max([oddSolution, evenSolution])

print answer("7")
print answer("100")
print answer("10000000000000")
print answer("1")
print answer("2")
print answer("5")
print answer("6")
