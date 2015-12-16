import random

with open('listfile', 'a') as f:
    l = []
    for m in range(1,100):
        for n in range(1,random.randint(1,100)):
            b = [random.randint(0,1000000),random.randint(0,1000000)]
            b.sort()
            if b[0] == b[1]:
                b[1] += 1
            l.append(b)
        f.write(str(l)+"\n")
        l = []
