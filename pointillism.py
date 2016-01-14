import fractions
import itertools
#I'd heard of this problem before and wouldn't swear that
#I found the answer myself the first time I saw it
def answer(vertices):
    minX = min([p[0] for p in vertices])
    maxX = max([p[0] for p in vertices])
    minY = min([p[1] for p in vertices])
    maxY = max([p[1] for p in vertices])
    corners = [[minX,minY], [maxX,maxY], [minX,maxY], [maxX, minY]]
    bounds = [[minX,minY],[maxX,maxY]]
    internalToBoundingBox = internalToBox(*bounds)
    cornerCount = len([p for p in vertices if corner(p, bounds)])
    edgeCount = len([p for p in vertices if edge(p, bounds)])
    print "corners and edges:", cornerCount, edgeCount
    total = internalToBoundingBox
    for c in itertools.combinations(vertices,2):
        total -= pointsOfRightTriangle(*c)
    if cornerCount == 2 and edgeCount == 0:
        print "corners, vertices", corners, vertices
        total -= offsetInternalVertex(vertices, corners)
    return total

def offsetInternalVertex(vertices, corners):
    internalVertex = [v for v in vertices if not v in corners][0]
    offCorners = [p for p in corners if p not in vertices]
    return min([halfSidedBox(p, internalVertex) for p in offCorners])

def halfSidedBox(point1, point2):
    width = abs(point1[0]-point2[0])
    height = abs(point1[1]-point2[1])
    if 0 in [width, height]:
        return 0
    else:
        return (width-1)*(height-1) + width + height -1 

def internalToBox(point1, point2):
    width = abs(point1[0]-point2[0])
    height = abs(point1[1]-point2[1])
    print "internal box:", point1, point2, width, height, (width-1)*(height-1)
    if 0 in [width, height]:
        return 0
    else:
        return (width-1)*(height-1)

def pointsOfRightTriangle(vertex1,vertex2):
    width = abs(vertex1[0]-vertex2[0])
    height = abs(vertex1[1]-vertex2[1])
    if 0 in [width, height]:
        return 0
    rectInternal = (width-1)*(height-1)
    hypoteneusePoints = fractions.gcd(height,width)-1
    print "right triangle:", vertex1, vertex2, width, height, (rectInternal + hypoteneusePoints)/2
    return (rectInternal + hypoteneusePoints)/2
    
def corner(vertex, bounds):
    xEdge = vertex[0] in [bounds[0][0], bounds[1][0]]
    yEdge = vertex[1] in [bounds[0][1], bounds[1][1]]
    return xEdge and yEdge
    
def edge(vertex, bounds):
    xEdge = vertex[0] in [bounds[0][0], bounds[1][0]]
    yEdge = vertex[1] in [bounds[0][1], bounds[1][1]]
    return (xEdge or yEdge) and not corner(vertex, bounds)

#print answer([[0, 0], [4, 0], [4, 8]])
#print answer([[0, 0], [5, 0], [4, 8]])
#print answer([[0,-1], [5, 0], [4, 8]])
#print answer([[2, 3], [6, 9], [7, 16]])
#print answer([[2, 3], [6, 9], [8, 16]])
print answer([[2, 3], [6, 9], [10, 160]])
#print answer( [[91207, 89566], [-88690, -83026], [67100, 47194]])
