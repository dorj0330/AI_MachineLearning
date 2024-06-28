theListA = []
theListB = []

for x in range(2, 1001, 2):
    theListA.append(x)

    
for x in range(3, 1001, 3):
    theListB.append(x)

def _union():
    theUnion = []
    for x in theListA:
        if x not in theUnion:
            theUnion.append(x)
    for x in theListB:
        if x not in theUnion:
            theUnion.append(x)
    return len(theUnion)


def _inter():
    theInter = []
    for x in theListA:
        for y in theListB:
            if(x==y):
                theInter.append(x)
                break
    return theInter

def _range():
    theRange = []
    for x in theListA:
        theRange.append(x)
    for x in theListB:
        theRange.append(x)
    return len(theRange)

def _mean():
    return sum(_inter())/len(_inter())

def _variance():
    mean = _mean()
    theInter = _inter()
    diff_squares = []
    for x in theInter:
        diff_squares.append((x - mean)**2)
    return sum(diff_squares) / (len(theInter))

def _standard_deviation():
    variance = _variance()
    return variance ** 0.5


print("Union:", _union())
print("Inter:", len(_inter()))
print("Mean of Intersection:", _mean())
print("Range:", _range())
print("Variance:", _variance())
print("Standard Deviation:", _standard_deviation())