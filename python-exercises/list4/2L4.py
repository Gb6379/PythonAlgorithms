import os
import time
import random

list = []
fulfill = 0
verifying = 0
while fulfill < 50:
    list.append(random.randint(-50, 50))
    fulfill += 1
print("Filling list...")
time.sleep(2)
print(list)
print("List filled")
print("Getting the positive numbers...")
time.sleep(2)
while (verifying < len(list)):
    if list[verifying] > 0:
        print("Negative Numbers of the list:")
        print(list[verifying])
    verifying += 1
os.system('pause')
