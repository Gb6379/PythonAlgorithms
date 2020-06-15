import os
import time
import random

list = []
sum = 0
fulfill = 0

while fulfill < 15:
    list.append(random.randint(1, 100))
    fulfill += 1
print('List =>', list)

for num in list:
    sum = sum + num

average = sum / len(list)
print('list sum = ', sum, 'average =', average)
