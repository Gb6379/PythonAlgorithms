import time
import os
import random

list = []
fulfill = 0
verifying = 0
counter = 0

while fulfill < 20:  # it's gonna fulfill the list with 20 number from 1 to 100
    print("Filling list...")
    list.append(random.randint(1, 100))
    fulfill += 1
time.sleep(2)
print("Complete")
os.system('pause')

while(verifying < len(list)):  # will loop over the list length to count the pair numbers
    if list[verifying] % 2 == 0:
        print("Fetching for pair number...")
        time.sleep(1)
        print("Found:", list[verifying])
        counter += 1
    verifying += 1
print('Number of Pairs:', counter)
print('list =>', list)
os.system('pause')
