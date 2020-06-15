import time
import os
import random

list = []
value = 0
reference = 7

while value != -1:
    value = int(input('type a grade: '))
    list.append(value)
list.remove(-1)
print('grades =>', list)

# count the number of grades assigned to the list
for i in list:
    list.count(i)
print('grades read =', i)

# reverse the values
list.reverse()
print('reverse order =', list)

# sum the values
sum = sum(list)
print('sum = ', sum)

# value's mean
mean = sum/len(list)
print('mean=', mean)

# values above the mean
for i in list:
    if i > mean:
        print('value above the mean:', i)

# value below the reference
for i in list:
    if i < reference:
        print('value below reference of:', reference, '=>', i)
os.system('pause')
