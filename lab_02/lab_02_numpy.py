import numpy

theListA = numpy.arange(2, 1001, 2)
theListB = numpy.arange(3, 1001, 3)

def _union():
    return len(numpy.union1d(theListA, theListB))

def _inter():
    return numpy.intersect1d(theListA, theListB)

def _range():
    return len(numpy.concatenate((theListA, theListB)))

def _mean():
    return numpy.mean(_inter())

def _variance():
    return numpy.var(_inter())

def _standard_deviation():
    return numpy.std(_inter())

print("Union:", _union())
print("Inter:", len(_inter()))
print("Mean of Intersection:", _mean())
print("Range:", _range())
print("Variance:", _variance())
print("Standard Deviation:", _standard_deviation())
