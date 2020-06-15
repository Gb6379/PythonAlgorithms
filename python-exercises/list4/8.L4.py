import os
import time
import random

list = []
listPair = []
listOdd = []
fulfill = 0
pair = 0
odd = 0
counter = 0

print('Creating list..')
time.sleep(2)

while fulfill < 10:
    list.append(random.randint(1, 100))
    fulfill += 1
print('List created', list)

print('Calculation Pair numbers...')
time.sleep(2)

while pair < len(list):
    if list[pair] % 2 == 0:
        print('Pair found =', list[pair])
        listPair.append(list[pair])
        counter += 1
    pair += 1

print('Pair numbers =>', listPair, 'total = ', counter)

print('Calculation Odd numbers...')
time.sleep(2)

while odd < len(list):
    if list[odd] % 2 == 1:
        listOdd.append(list[odd])
        counter += 1
    odd += 1

print('Odd numbers =>', listOdd, 'Total =', counter)

os.system('pause')
