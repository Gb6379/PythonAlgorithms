import os
import random
import time
list = []
fulfill = 0
verifying = 0

while fulfill < 15:
    list.append(random.uniform(-45.6, 100.9))
    fulfill += 1
print(list)

while verifying < len(list):
    if list[verifying] < 0:
        print('Negative number index =>', verifying)
    verifying += 1
