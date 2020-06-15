import os
import time
import random

list = []
fullfill = 0

print("filling...")
time.sleep(2)

while fullfill < 30:
    list.append(random.randint(-100, 100))
    fullfill += 1
print('list =>', list)
print('lesser number of the list =', min(list))
print('Number`s Index/postion inside the list = ', list.index(min(list)))
os.system('pause')
