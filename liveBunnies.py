import copy

#new approach to try: recursively split the time domain down the middle
#then enumerate through the ones that cross the boundary 
# and find the best one on each side to bring together with it
#like the two-closest-points algorithm
def splitTimes(meetings):
    times = []
    for m in meetings:
        times.extend(m)
    times.sort()
    midpoint = times[len(times)/2]
    left, right, cross = [], [], []
    for [start, end] in meetings:
        if end <= midpoint:
            left.append([start,end])
        elif start >= midpoint:
            right.append([start,end])
        else:
            cross.append([start,end])
    left.sort(None, lambda x: x[1])
    right.sort(None, lambda x: x[0])
    return [left, cross, right]

def getMostMeetings(meetings):
    stack = [(meetings, 0, 1000000, [[0,1000000]])]
    lowBounds = [1000000]
    highBounds = [0]
    while len(stack):
        working = stack[-1]
        pivots = working[-1]
        lowestTop = min(x[1] for x in pivots)
        highestBottom = max(x[0] for x in pivots)

def answer(meetings):
    meetings.sort(None, lambda x: x[1]-x[0])
    b = recurseAnswer(meetings, [], [0])
    b.sort()
    print b
    return len(b)

def fitsIn(meetings, meeting):
    return all(map(lambda x: (x[1] <= meeting[0]) or (meeting[1] <= x[0]), meetings))

def tupleOfTuples(listOfLists):
    return tuple(tuple(x) for x in listOfLists)

def tupleOfTupleOfTuples(listOfListofLists):
    return tuple(tupleOfTuples(x) for x in listOfListofLists)

def recurseAnswer(potentialMeetings, chosenMeetings, bestSeen):
    if len(potentialMeetings) + len(chosenMeetings) < bestSeen[0]:
        return chosenMeetings
    elif len(potentialMeetings) ==0:
        if len(chosenMeetings) > bestSeen[0]:
            bestSeen[0] = len(chosenMeetings)
        return chosenMeetings
    candidate =  potentialMeetings.pop()
    no = recurseAnswer(copy.copy(potentialMeetings), copy.copy(chosenMeetings), bestSeen)
    if fitsIn(chosenMeetings, candidate):
        yes = recurseAnswer(copy.copy(potentialMeetings), chosenMeetings + [candidate], bestSeen)
    else:
        yes = []
    choices = [yes,no]
    choices.sort(key=lambda x: -len(x))
    #print "choices sorted:", choices
    return choices[0]


print fitsIn([[0,1]],[2,3]), True
print fitsIn([[0,4]],[2,3]), False
print fitsIn([[0,2], [3, 10]],[2,3]), True
print fitsIn([[0,3]],[2,4]), False
print fitsIn([[3, 10]],[2,4]), False

b = [[833014, 932759], [333361, 829630], [345926, 969193], [610527, 986211], [174101, 273921], [17929, 409821], [520434, 737077]]
c = [[152405, 725199], [56142, 623717], [172219, 605816], [41975, 697658],
    [434065, 589762], [359393, 679582], [50796, 636259], [134510, 474910],
    [817038, 954544], [522861, 624969], [225403, 765325], [236685, 973443],
    [273452, 596910], [158073, 331262], [731199, 974259], [475969, 619651],
    [197615, 256533], [260716, 741066], [179358, 322627], [174981, 309989],
    [349456, 404190], [229193, 562949], [148050, 190646], [446477, 712211],
    [232839, 363414], [274734, 726413], [180957, 880176], [361683, 693281],
    [47098, 940261], [307655, 628442], [241107, 433310], [395237, 531134],
    [444050, 663860], [27615, 280486], [390551, 558692], [269390, 729684]]
d = [[426483, 433381], [134842, 561043], [227975, 412555], [141030, 485790], [310709, 614373], [137691, 267683], [197093, 202259], [508955, 595637], [105654, 935310], [266655, 790889], [49056, 793795], [276842, 894281], [722882, 789548], [363798, 654825], [96194, 199328], [559001, 630173], [693868, 928727], [180897, 226520], [205466, 990882], [400365, 991035], [584026, 859182], [485800, 876766], [105192, 222211], [357307, 681002], [423261, 643879], [220594, 697148], [298418, 553436], [384315, 804993], [463309, 968939], [6540, 110301], [253180, 887372], [518738, 906152], [472351, 685116], [498245, 957839], [370952, 678533], [593291, 633758], [231458, 560360], [464230, 967168], [896521, 957451], [524098, 530342], [115072, 140983], [38624, 109291], [563323, 819192], [176024, 908047], [455652, 866041], [42253, 132160], [117667, 358568], [215945, 931646], [438412, 702746], [174093, 175537], [119665, 486380], [535510, 935934], [397096, 623055], [638010, 937878], [129126, 805617], [35025, 395120], [135638, 704094], [378441, 549462], [239949, 573971], [221048, 222690], [946704, 963305], [536246, 852885], [19658, 98897], [106811, 530867], [145221, 788250], [165061, 620440], [213976, 545922], [134481, 327824], [388954, 647397], [383708, 463675], [318845, 839220], [501960, 902122], [313369, 742891], [39577, 311203], [11213, 394602], [448851, 811061], [165538, 527279], [663831, 741389], [179009, 432446], [40590, 224182], [101316, 876724]]
e = list([x, x+1] for x in range(1, 1001, 10))
print answer(b)
b.sort
print b
print answer(c)
c.sort
print c
print answer(d)
d.sort
print d, len(d)
print answer(e)
e.sort
print e, len(e)



#2: top_end       = 4500
#1: top_end_less  = 3010
#0: top_end_least = 0
#
#pivots = [3000, 5005], [5000, 6000], nil
#median = 5000
#
#2: bottom_end      = 5004
#1: bottom_end_more = 5500
#0: bottom_end_most = 10000
#
#
#[3000, 5005]: 2, bottom: 3000, top: ???
#[5000, 6000]: 3, top: 6000, bottom: ???
#         nil: 4, top: ???, bottom: ???
#
#
#work from the right edge
#[[17929, 409821], [148050, 190646], [174101, 273921], [197615, 256533], 
#[333361, 829630], [345926, 969193], [349456, 404190], [520434, 737077], 
#[522861, 624969], [610527, 986211], [817038, 954544]]
#
#1000000: 0
#817038: 1, 1000000: 0
#nil
#522861: 2, 817038: 1, 1000000: 0
#nil
#349456: 3, 522861: 2, 817038: 1, 1000000: 0
#nil
#nil
#197615: 4, 349456: 3, 522861: 2, 817038: 1, 1000000: 0
#nil
#148050: 5, 197615: 4, 349456: 3, 522861: 2, 817038: 1, 1000000: 0
#nil
#
#[[148050, 190646], [197615, 256533], [174101, 273921], [349456, 404190], 
#[17929, 409821], [522861, 624969], [520434, 737077], [333361, 829630], 
#[817038, 954544], [345926, 969193], [610527, 986211]]
#
#0: 0
#190646: 1
#256533: 2
#-
#404190: 3
#-
#624969: 4
#-
#-
#954544: 5
#-
#-
