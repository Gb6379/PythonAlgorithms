import os
import random
import time

list = []

fulfill = 0
counter = 0
while fulfill < 10:
    list.append(random.randint(1, 100))
    fulfill += 1
print('List =', list)

value = int(input("Type a value\n"))

for i in list:
    if value == i:
        print('Exist, position =', list.index(i))
        break
    else:
        os.system('cls')
        print('value doesnt exist')
os.system('pause')
