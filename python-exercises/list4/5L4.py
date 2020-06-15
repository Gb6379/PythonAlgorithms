import os
import time
import random

list = []
fulfill = 0

print('Filling...')
time.sleep(1)
while fulfill < 20:
    list.append(random.randint(1, 30))
    fulfill += 1
print('Normal list =>', list)
print('Reversing...')
time.sleep(1)
list.reverse()
print('Backwards list =>', list)
os.system('pause')
