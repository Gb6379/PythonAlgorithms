import time
import os
import random

listX = []
listY = []
listZUnion = []
listZDiff = []
listZSum = []
listZProd = []
listInter = []

fulfill = 0

while fulfill < 10:
    listX.append(random.randint(1, 100))
    listY.append(random.randint(1, 100))
    fulfill += 1
setX = set(listX)  # convert a list into a set
setY = set(listY)


print('Structure X =>', setX)
print('Structure Y =>', setY)

# union
listZUnion.append(setX.union(setY))
print('Union X and Y =>', listZUnion)

# difference
listZDiff.append(setX.difference(setY))
print('Diferente X and Y =>', listZDiff)

# sum
x = sum(listX)
y = sum(listY)
print('sum list X =', x, 'sum list Y =', y)
listZSum.append(x + y)
print('Sum X and Y =>', listZSum)

# product
listZProd.append(x*y)
print('Product X Y =', listZProd)

# intersection
listInter.append(setX.intersection(setY))
print('intersection X Y = ', listInter)


os.system('pause')
